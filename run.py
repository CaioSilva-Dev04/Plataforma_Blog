#Esse é o ponto de partida  da aplicação. sempre que rodarmos (python run.py, o servidor sobe.

from app import app # Importância do flask que cria no pacote (app).

if __name__ == "__main__": #garante que o servidor só rode se o arquivo for executado diretamente. 
    app.run(debug=True) # Inicia o servidor Flak. O (debug=Tue) mostra erros detalhados e recarrega automaticamente quando vc altera o código.