from fastavro import writer, parse_schema

schema = {
    "type": "record",
    "name": "Number",
    "fields": [{"name": "value", "type": "int"}],
}

# Parse the schema
parsed_schema_v1 = parse_schema(schema)

# Data to serialize
data_v1 = [{"value": 10}, {"value": 20}]

# Serialize data
with open("data/numbers.avro", "wb") as out_file:
    writer(out_file, parsed_schema_v1, data_v1)

print("Data serialized with version 1 of the schema.")


# Evolved schema with a new optional field 'description'
schema_v2 = {
    "type": "record",
    "name": "Number",
    "fields": [
        {"name": "value", "type": "int"},
        {
            "name": "description",
            "type": ["null", "string"],
            "default": "null",
        },  # New field with default
    ],
}

# Parse the schema
parsed_schema_v2 = parse_schema(schema_v2)

# Data to serialize
data_v2 = [{"value": 10, "description": "ten"}, {"value": 20}]

# Serialize data
with open("data/numbers2.avro", "wb") as out_file:
    writer(out_file, parsed_schema_v2, data_v2)

print("Data serialized with version 2 of the schema.")
