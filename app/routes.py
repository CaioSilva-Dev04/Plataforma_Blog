#Esse arquivo é responsável por mapear URLs para funções. Cada rota será uma página ou funcionalidade do blog.

from app import app  # Importa a instância do Flask criada em __init__.py.

@app.route("/") # Define uma rota. O / significa a página inicial do site.
def home(): # Função que será executada quando alguém acessar /.
    return "Bem-vindo ao Blog!" # Resposta enviada ao navegador (por enquanto, só texto).

from app import app 
from flask import render_template # Importa a função que carrega templates HTML.

@app.route("/") # Rota da página inicial.
def home():
    return render_template("home.html") # Renderiza o arquivo (templates/home.html) e envia o HTML ao navegador.