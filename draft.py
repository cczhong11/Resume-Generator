import json
for filename in ["ProjectJson/cloud.json","ProjectJson/ds.json","ProjectJson/searchengine.json","ProjectJson/other.json",]:
        print(filename)
        with open(filename, 'r') as f:
            obj = json.load(f)
        for i in obj:
            name = i["name"]
            date = i['date']
            place = i['place']
            title = i['title']
            tech = i['tech']
            print(name+":"+", ".join(tech))