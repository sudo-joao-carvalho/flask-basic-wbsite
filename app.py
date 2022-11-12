from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/') #para dar start: (terminal) python3 "app.py"
def home(): #name parameter
    #return render_template("index.html") , content = name, r = 2 --> para o caso de ter <name> no route
    #PARA PASSAR UMA LISTA
    return render_template("index.html", content = ["joao", "barradas", "gonzo"])

"""
@app.route('/<name>')
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin")) #dentro do url_for fazia sentido por um url mas mete se o nome da funcao para a qual queremos dar redirect // usa-se para o caso de alguem tentar aceder a um site que nao e suposto logo e redirecionado
"""

if __name__ == "__main__":
    app.run()