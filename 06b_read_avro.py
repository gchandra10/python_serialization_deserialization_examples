import fastavro

# Path to your Avro file
avro_file_path = "data/friends_simple_data.avro"

# Open the Avro file and read the records
with open(avro_file_path, "rb") as avro_file:
    reader = fastavro.reader(avro_file)
    schema = reader.writer_schema
    # print("Schema:", schema)

    for index, record in enumerate(reader, 1):
        print(index, record, "\n")

print("*" * 100)

# Path to your Avro file
avro_file_path = "data/friends_nested_data.avro"

# Open the Avro file and read the records
with open(avro_file_path, "rb") as avro_file:
    reader = fastavro.reader(avro_file)
    schema = reader.writer_schema
    # print("Schema:", schema)

    for index, record in enumerate(reader, 1):
        print(index, record, "\n")
