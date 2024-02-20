from friends_data import friends_json_data
import json

obj_data = friends_json_data()
friends_data = obj_data.simple_data().get("characters")

# Serialize to JSON
with open("data/friends.json", "w") as json_file:
    json.dump(friends_data, json_file)
