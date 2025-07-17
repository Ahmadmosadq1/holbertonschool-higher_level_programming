import json
with open('items.json', 'r') as file:
    content = json.load(file)
item_list = content['items']


