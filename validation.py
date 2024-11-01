import json

with open(r'D:\Code\Projects\NPTEL-QUIZ\Resources\data.json', encoding='utf-8') as f:
    data = json.load(f)


data = data['questions']
counter = {}

for question in data:
    c = str(question['year']) + '.' + str(question['week'])
    if c in counter:
        counter[c] += 1
    else:
        counter[c] = 1

for key, value in counter.items():
    print(key, value)
