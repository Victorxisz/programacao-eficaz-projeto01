from utils import load_data, load_template, load_note
import sqlite3

def index():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM note ORDER BY markdown DESC")
    dados = cursor.fetchall()
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(
            title=linha[1],
            details=linha[2],
            id=linha[0], 
            markdown_icon=("bi-bookmark-fill" 
                            if linha[3]==1
                            else "bi-bookmark"))
        for linha in dados
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(title, details):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO note (title,content) values (?,?)",(title,details))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM note WHERE id=?",(id,))
    conn.commit()
    conn.close()

def get_note(id):
    return load_note(id)

def edit(note):
    return load_template("edit.html").format(id=note.id, title=note.title, content=note.content)

def update(id, new_title, new_content):
    print(f"oi {new_title}")
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE note SET title = ?, content = ? WHERE id = ?",(new_title, new_content, id))
    conn.commit()
    conn.close()

def markdown(note_id):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE note SET markdown = NOT markdown WHERE id= ?", (note_id,))
    conn.commit()
    conn.close()