from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/') #para dar start: (terminal) python3 "app.py"
def home(): #name parameter
    #return render_template("index.html") , content = name, r = 2 --> para o caso de ter <name> no route
    #PARA PASSAR UMA LISTA
    return render_template("index.html", content = ["joao", "barradas", "gonzo"])

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"] #name of the input in html
        return redirect(url_for("user", usr = user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

"""
@app.route('/<name>')
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin")) #dentro do url_for fazia sentido por um url mas mete se o nome da funcao para a qual queremos dar redirect // usa-se para o caso de alguem tentar aceder a um site que nao e suposto logo e redirecionado
"""

if __name__ == "__main__":
    app.run(debug = True) #debug = True --> permite que nao tenhamos que estar sempre a dar re run ao servidor smp que alteramos alguma coisa