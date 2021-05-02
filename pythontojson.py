import json

json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'

data = json.loads(json_data)
for x in data:
    print("%s : %d" %(x, data[x]))


with open('exmple.json', 'r') as f:
    dict = json.load(f)

for i in dict:
    print(i['Name'])
