from flask import Flask, request, jsonify
import time
from bot import Bot
from config import definindo_webhook

"""
Por ser o arquivo primário e de iniciação eu tentei deixar o mais limpo e claro possível.
Importei o Flask, uma das formas que eu achei pra criar um servidor no computador
Posso estar errado sobre ele pois não fiz muitas pesquisas, o request para requisições e 
Ter acesso ao que o Telegram envia para o meu link e o jsonify para transformar minhas 
Respostas para o servidor em Json.
"""
app = Flask(__name__) #Padrão para criação de um objeto do tipo Flask fazendo com que o programa tenha WSGI
Bot.init_webhook(definindo_webhook)

@app.route('/webhook', methods=['POST']) #Programando para que o servidor recuse outros metodos no caminho /webhook
def index():
    req = request.get_json()#Pega o que foi enviado pelo Telegram
    bot = Bot()#Instacia o bot do arquivo bot.py importado no inicio
    bot.passando_dados(req)#Passa os dados da requisição para ser trabalhado.
    time.sleep(5)#Coloquei esse sleep pois a API do google estava dando erro e ele ajudou a cortar um pouco dos erros.
    success = bot.action()#Aqui ele trata o dado e retorna o código da operação, isso pode ser melhor entendido em HTML onde o código 200 indica que tudo foi certo.
    return jsonify(success=success) #Retornando o código para o Telegram. (posso estar errado)

if __name__ == '__main__': #Estabelece a porta, o telegram recomenda conexão com as portas: 443, 80, 88, 8443. Assim ele roda no 127.0.0.0:8443
    app.run(port=8443)

'''
Algumas partes eu não afirmo com tanta certeza pois a documentação me deixou confuso
Assim que eu atualizar o código eu trago com mais clareza.
'''
