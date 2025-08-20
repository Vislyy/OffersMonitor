import json

def write_template(data):
    with open("data/templates.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def read_template():
    try:
        with open("data/templates.json", "w", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except:
        return {}