## pip install fastavro

from fastavro import schemaless_writer, schemaless_reader
from io import BytesIO

#BytesIO is an in-memory stream for bytes, helps to write/read bytes without using actual files.

# Define the Avro schema
schema = {
    "type": "record",
    "name": "Person",
    "fields": [{"name": "name", "type": "string"}, {"name": "age", "type": "int"}],
}

# Data to be serialized
data = {"name": "Rachel Green", "age": 30}

# Serialize the data to Avro bytes using schemaless_writer
# encode data using the schema and writte to a bytes buffer in memory
bytes_buffer = BytesIO()
schemaless_writer(bytes_buffer, schema, data)


# Get the bytes
avro_bytes = bytes_buffer.getvalue()
print("Serialized Avro bytes:", avro_bytes)


# Deserialize the Avro bytes back to a Python dictionary

bytes_buffer.seek(0)  # Reset the buffer's position to the beginning
deserialized_data = schemaless_reader(bytes_buffer, schema)

print("Deserialized data:", deserialized_data)
