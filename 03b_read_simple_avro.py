from fastavro import reader, parse_schema

schema = {
    "type": "record",
    "name": "Number",
    "fields": [{"name": "value", "type": "int"}],
}

parsed_schema_v1 = parse_schema(schema)
# Read data using the schema
with open("data/numbers.avro", "rb") as in_file:
    for record in reader(in_file, reader_schema=parsed_schema_v1):
        print(record)

print(
    "Data deserialized with version 1 of the schema, showing default values for new fields."
)
