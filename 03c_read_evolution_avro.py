from fastavro import reader, parse_schema

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

parsed_schema_v2 = parse_schema(schema_v2)
# Read data using the schema
with open("data/numbers.avro", "rb") as in_file:
    for record in reader(in_file, reader_schema=parsed_schema_v2):
        print(record)

print(
    "Data deserialized with version 2 of the schema, showing default values for new fields."
)


# Further evolved schema with an array field 'tags'
schema_v3 = {
    "type": "record",
    "name": "Number",
    "fields": [
        {"name": "value", "type": "int"},
        {"name": "description", "type": ["null", "string"], "default": None},
        {
            "name": "tags",
            "type": {"type": "array", "items": "string"},
            "default": [],
        },  # New array field with default
    ],
}

parsed_schema_v3 = parse_schema(schema_v3)
# Read data using the schema
with open("data/numbers.avro", "rb") as in_file:
    for record in reader(in_file, reader_schema=parsed_schema_v3):
        print(record)

print(
    "Data deserialized with version 3 of the schema, showing default values for new fields."
)
