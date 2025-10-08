from friends_data import friends_json_data
import json

obj_data = friends_json_data()

friends_data = obj_data.simple_data().get("characters")

friends_nested_data = obj_data.nested_data()


# Serialize to JSON
with open("data/friends_data.json", "w") as json_file:
    json.dump(friends_data, json_file)
    
with open("data/friends_nested.json", "w") as json_file2:
    json.dump(friends_nested_data, json_file2)
