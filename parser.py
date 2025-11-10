import json

file = open("all_properties_question_scored.json", "r")
data = file.read()
json_data = json.loads(data)

formatted_data = {}

for prop, scores in json_data.items():
    formatted_data[prop] = {}
    for score in scores:
        noun = score[0]
        value = score[1]
        formatted_data[prop][noun] = value
        
property_table = {}
threshold = 5
for prop, noun_scores in formatted_data.items():
    property_table[prop] = []
    for noun, score in noun_scores.items():
        if score>=threshold:
            property_table[prop].append(noun)
            
json_str = json.dumps(property_table)

with open("property_table.json", "w") as f:
    f.write(json_str)
        
