import json, time
from fastavro import schemaless_writer, schemaless_reader
from io import BytesIO
from db_config import get_redis_connection

r = get_redis_connection()
# r.flushall()

# Define a sample data structure
data = {
    "users": [
        {"name": "John Doe", "age": 30, "email": "johndoe@example.com"},
        {"name": "Jane Doe", "age": 25, "email": "janedoe@example.com"},
        {"name": "Alice Johnson", "age": 27, "email": "alicej@example.com"},
        {"name": "Bob Smith", "age": 22, "email": "bobsmith@example.com"},
        {"name": "Charlie Brown", "age": 28},  # Email will use default value (null)
        {"name": "Dana Scully", "age": 32, "email": "dscully@example.com"},
        {"name": "Evan Wright", "age": 29, "email": "evanw@example.com"},
        {"name": "Fiona Glenanne", "age": 35, "email": "fionag@example.com"},
        {"name": "Greg House", "age": 40, "email": "gregh@example.com"},
        {"name": "Hannah Abbott", "age": 24},  # Email will use default value (null)
    ]
}

# Define the Avro schema
schema = {
    "type": "record",
    "name": "Users",
    "fields": [
        {
            "name": "users",
            "type": {
                "type": "array",
                "items": {
                    "type": "record",
                    "name": "User",
                    "fields": [
                        {"name": "name", "type": "string"},
                        {"name": "age", "type": "int"},
                        {
                            "name": "email",
                            "type": ["null", "string"],
                            "default": "null",
                        },
                    ],
                },
            },
        },
    ],
}


# Function to serialize data with Avro
def avro_serialize(data, schema):
    bytes_buffer = BytesIO()
    schemaless_writer(bytes_buffer, schema, data)
    return bytes_buffer.getvalue()


# Function to deserialize data with Avro
def avro_deserialize(serialized_data, schema):
    # Ensure serialized_data is bytes; this should already be the case.
    if isinstance(serialized_data, str):
        # If for some reason it's a str, convert it back to bytes.
        serialized_data = serialized_data.encode("utf-8")

    bytes_buffer = BytesIO(serialized_data)

    return schemaless_reader(bytes_buffer, schema)


# Function to benchmark Avro serialization with Redis
def benchmark_avro(data, schema):
    ## Storing Avro data in Redis
    serialized_data = avro_serialize(data, schema)
    start_time_store = time.time()
    r.set("user:avro", serialized_data)
    end_time_store = time.time()

    ## Reading Avro data from Redis
    start_time_retrieve = time.time()
    retrieved_data = r.get("user:avro")
    deserialized_data = avro_deserialize(retrieved_data, schema)
    end_time_retrieve = time.time()

    ## Print the values as rows
    print("Displaying Avro Data \n")

    for index, record in enumerate(deserialized_data["users"], 1):
        print(index, record, "\n")

    print(
        f"Avro - Store time: {end_time_store - start_time_store}, Retrieve time: {end_time_retrieve - start_time_retrieve} \n"
    )


# Function to benchmark JSON serialization with Redis
def benchmark_json(data):
    ## Storing JSON data in Redis
    start_time_store = time.time()
    serialized_data_json = json.dumps(data).encode("utf-8")
    r.set("user:json", serialized_data_json)
    end_time_store = time.time()

    ## Reading Json data in Redis
    start_time_retrieve = time.time()
    retrieved_data_json = r.get("user:json")
    if isinstance(retrieved_data_json, bytes):
        retrieved_data_json = retrieved_data_json.decode("utf-8")

    deserialized_data_json = json.loads(retrieved_data_json)
    end_time_retrieve = time.time()

    ## Print the values as rows
    print("Displaying JSON Data \n")

    for index, record in enumerate(deserialized_data_json["users"], 1):
        print(index, record, "\n")
    print(
        f"JSON - Store time: {end_time_store - start_time_store}, Retrieve time: {end_time_retrieve - start_time_retrieve}"
    )


# Run benchmarks
benchmark_avro(data, schema)
benchmark_json(data)

# List of keys to check memory usage for
keys = ["user:avro", "user:json"]

# Iterate over keys and print memory usage
for key in keys:
    memory_usage = r.memory_usage(key)
    print(f"\n Memory usage for {key}: {memory_usage} bytes")