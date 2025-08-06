import json
with open("json_data.json") as json_file:
    data = json.load(json_file)
    print("Type", type(data))

import json
jsonString = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'
studentinfo =json.loads(jsonString)
print(studentinfo)
print(studentinfo['id'])