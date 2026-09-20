# Esse arquivo é o núcleo da aplicação. Ela inicia o Flak e carrega rotas.

from flask import Flask # Importa a classe principal do Flask.

app = Flask(__name__) # Cria a aplicação Flask. O parâmetro (__name__) ajuda o Flask a localizar recursos (Tamplates, estáticos).

from app import routes # Importa as rotas definidas em (routes.py). Isso conecta os caminhos da web ao servitor.