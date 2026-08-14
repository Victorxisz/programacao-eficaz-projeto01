import json

def load_data(name):
    file_path = f"static/data/{name}"
    with open(file_path, 'r', encoding="utf-8") as data:
        content = json.load(data)
        return (content)

def load_template(name):
    file_path = f"static/templates/{name}"
    with open(file_path, "r", encoding="utf-8") as html:
        template = html.read()
        return template