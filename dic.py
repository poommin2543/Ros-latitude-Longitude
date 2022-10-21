import json
str = "{'latitude': 'latitude1', 'longitude': 'longitude1'}"
# print(type(str))
# res = ast.literal_eval(str)
# print(type(res))
# print(res['latitude'])

# sp = str['latitude']

# print(sp)

print(type(json.loads(str)))