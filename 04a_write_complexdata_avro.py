from fastavro import writer, parse_schema, reader

# Define the schema in Python
schema = {
    "type": "record",
    "name": "IntermediateExample",
    "fields": [
        {"name": "id", "type": "bytes"},
        {
            "name": "status",
            "type": {
                "type": "enum",
                "name": "Status",
                "symbols": ["ACTIVE", "INACTIVE", "UNKNOWN"],
            },
        },
        {"name": "properties", "type": {"type": "map", "values": "string"}},
        {"name": "description", "type": ["null", "string"], "default": "null"},
        {
            "name": "fixedSizeData",
            "type": {"type": "fixed", "size": 4, "name": "FixedSize"},
        },
    ],
}

parsed_schema = parse_schema(schema)

# Data conforming to the schema
record = [
    {
        "id": b"\x00\x00\x00\x01",
        "status": "ACTIVE",
        "properties": {"key1": "value1", "key2": "value2"},
        "description": "First record",
        "fixedSizeData": b"\x01\x00\x00\x00",
    },
    {
        "id": b"2",
        "status": "ACTIVE",
        "properties": {"key1": "value3", "key2": "value4"},
        "description": "Second record",
        "fixedSizeData": b"ABCD",
    },
]


# Serialize the data
with open("data/complex_data_example.avro", "wb") as out_file:
    writer(out_file, parsed_schema, record)

print("Data serialized to intermediate_example.avro. \n\n")


# Read the data
with open("data/complex_data_example.avro", "rb") as in_file:
    for index, record in enumerate(reader(in_file)):
        print(index, record, "\n")
