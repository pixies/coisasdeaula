from flask import Flask

#criando aplicacao web do tipo flask
app = Flask(__name__)

#DEFINIR NOSSOS CAMINHOS - ROTAS - ROUTE
@app.route("/home")
@app.route("/")
def index():
    return "Pagina Inicial - HOME"

@app.route("/contato")
def contato():
    return "Pagina de contato"

@app.route("/login")
def login():
    return "Pagina de login"

@app.route("/soma/<int:v1>/<int:v2>")
def soma(v1,v2):
    soma = v1 + v2
    return str(soma)

@app.route("/mult/<int:v1>/<int:v2>")
def mult(v1,v2):
    mult = v1*v2
    return str(mult)

if __name__ == '__main__':
    app.run(debug=True)
