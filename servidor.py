from flask import Flask, render_template_string, request, redirect
import views


app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'
    views.submit(titulo, detalhes)
    return redirect('/')

@app.route("/delete", methods=["POST"])
def delete_note():
    note_id = request.form.get("id")
    print(note_id)
    views.delete(id=note_id)
    return redirect('/')

@app.route("/update/<int:note_id>", methods=["GET"])
def edit_note(note_id):
    note=views.get_note(note_id)
    return render_template_string(views.edit(note))

@app.route("/update/<int:note_id>", methods=["POST"])
def update_note(note_id):
    new_title = request.form.get("titulo")
    new_content = request.form.get("detalhes")
    views.update(note_id, new_title, new_content)
    return redirect("/")

@app.route("/markdown/<int:note_id>", methods=['POST'])
def markdown_note(note_id):
    views.markdown(note_id)
    return redirect("/")
if __name__ == '__main__':
    app.run(debug=True)
