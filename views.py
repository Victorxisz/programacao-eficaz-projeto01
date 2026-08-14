from utils import load_data, load_template
import json
def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(title, details):
    with open("static/data/notes.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    dados.append({'titulo':title,'detalhes': details})
    print(dados)

    with open("static/data/notes.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo)