from fastavro import reader, parse_schema

schema = {
    "type": "record",
    "name": "Number",
    "fields": [{"name": "value", "type": "int"}],
}

print("Avro data without Schema\n")
# Read data without using schema
with open("data/numbers.avro", "rb") as in_file:
    for record in reader(in_file):
        print(record)

print("-" * 100)

print("Avro data Using Schema\n")
# Read data using the schema
parsed_schema_v1 = parse_schema(schema)

with open("data/numbers.avro", "rb") as in_file:
    for record in reader(in_file, reader_schema=parsed_schema_v1):
        print(record)

print(
    "\n Data deserialized with version 1 of the schema."
)
