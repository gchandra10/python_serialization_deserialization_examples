from fastavro import writer, reader, parse_schema

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
