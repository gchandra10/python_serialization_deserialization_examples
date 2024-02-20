import json
import fastavro
from fastavro.schema import load_schema, parse_schema
from friends_data import friends_json_data


def infer_avro_type(value, field_name="Field"):
    if isinstance(value, str):
        return ["null", "string"]
    elif isinstance(value, int):
        return ["null", "int"]
    elif isinstance(value, float):
        return ["null", "float"]
    elif isinstance(value, list):
        # Assume all elements of the list are of the same type
        if value:
            return ["null", {"type": "array", "items": infer_avro_type(value[0])}]
        else:
            return ["null", {"type": "array", "items": "null"}]
    elif isinstance(value, dict):
        fields = []
        for k, v in value.items():
            field_type = infer_avro_type(v, k)
            fields.append({"name": k, "type": field_type, "default": None})
        return [
            "null",
            {
                "type": "record",
                "name": "AutoGenRecord_" + k + field_name,
                "fields": fields,
            },
        ]
    elif value is None:
        return "null"
    else:
        return ["null", "string"]  # Default to string for unknown types


# Function to generate Avro schema from a JSON object
def generate_avro_schema_from_json(json_obj):
    return infer_avro_type(json_obj)


def convert_avro(datatype):
    obj_data = friends_json_data()

    if datatype == "Simple":
        friends_data = obj_data.simple_data().get("characters")
        avro_filename = "friends_simple_data.avro"
        data = [friends_data]
        # Generate the Avro schema based directly on the Python data structure
        # avro_schema = generate_avro_schema_from_json(friends_data)
        # print(avro_schema)

        avro_schema = {
            "type": "record",
            "name": "AutoGenRecord_ageField",
            "fields": [
                {"name": "name", "type": ["null", "string"], "default": "null"},
                {"name": "job", "type": ["null", "string"], "default": "null"},
                {"name": "age", "type": ["null", "int"], "default": None},
            ],
        }

    elif datatype == "Nested":
        friends_data = obj_data.nested_data()  # Assuming this returns a list of records
        avro_filename = "friends_nested_data.avro"

        data = [friends_data]
        avro_schema = {
            "type": "record",
            "name": "Friends",
            "fields": [
                {"name": "name", "type": ["string", "null"], "default": "null"},
                {"name": "occupation", "type": ["string", "null"], "default": "null"},
                {
                    "name": "relationship_status",
                    "type": ["string", "null"],
                    "default": "null",
                },
                {
                    "name": "friends",
                    "type": ["null", {"type": "array", "items": "string"}],
                    "default": "null",
                },
                {
                    "name": "education",
                    "type": [
                        "null",
                        {
                            "type": "record",
                            "name": "Education",
                            "fields": [
                                {
                                    "name": "high_school",
                                    "type": ["string", "null"],
                                    "default": "null",
                                },
                                {
                                    "name": "college",
                                    "type": ["string", "null"],
                                    "default": "null",
                                },
                                {
                                    "name": "degree",
                                    "type": ["string", "null"],
                                    "default": "null",
                                },
                                {
                                    "name": "culinary_school",
                                    "type": ["string", "null"],
                                    "default": "null",
                                },
                                {
                                    "name": "drama_school",
                                    "type": ["string", "null"],
                                    "default": "null",
                                },
                            ],
                        },
                    ],
                    "default": "null",
                },
                {
                    "name": "employment_history",
                    "type": [
                        "null",
                        {
                            "type": "array",
                            "items": {
                                "type": "record",
                                "name": "Employment",
                                "fields": [
                                    {
                                        "name": "company",
                                        "type": ["string", "null"],
                                        "default": "null",
                                    },
                                    {
                                        "name": "position",
                                        "type": ["string", "null"],
                                        "default": "null",
                                    },
                                    {
                                        "name": "years",
                                        "type": ["string", "null"],
                                        "default": "null",
                                    },
                                    {
                                        "name": "show",
                                        "type": ["string", "null"],
                                        "default": "null",
                                    },
                                    {
                                        "name": "role",
                                        "type": ["string", "null"],
                                        "default": "null",
                                    },
                                ],
                            },
                        },
                    ],
                    "default": "null",
                },
                {
                    "name": "children",
                    "type": [
                        "null",
                        {
                            "type": "array",
                            "items": {
                                "type": "record",
                                "name": "Child",
                                "fields": [
                                    {"name": "name", "type": "string"},
                                    {"name": "mother", "type": "string"},
                                ],
                            },
                        },
                    ],
                    "default": "null",
                },
                {"name": "spouse", "type": ["string", "null"], "default": "null"},
            ],
        }

    with open(f"data/{avro_filename}", "a+b") as avro_file:
        parsed_schema = fastavro.parse_schema(avro_schema)
        for record in data:
            try:
                fastavro.writer(avro_file, parsed_schema, record)
            except ValueError as e:
                print(f"Error processing record: {record}")
                print(f"Error message: {e}")
                continue


convert_avro("Simple")
convert_avro("Nested")
