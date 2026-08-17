from utils import load_data, load_template
import json
import sqlite3

def index():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM note")
    dados = cursor.fetchall()
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=linha[1], details=linha[2], id=linha[0])
        for linha in dados
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(title, details):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO note (title,content) values (?,?)",(title,details))
    conn.commit()
    id_usuario = cursor.lastrowid
    conn.close()

def delete(id):
    print(id)
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM note WHERE id=?",(id,))
    conn.commit()
    conn.close()
    