import json
import sqlite3

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

class Note:
        def __init__(self, id, title, content):
            self.id = id
            self.title = title
            self.content = content

    
def load_note(id):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM note WHERE id=?", (id,))
    loaded_note=cursor.fetchone()
    note = Note(loaded_note[0], loaded_note[1], loaded_note[2])
    return note