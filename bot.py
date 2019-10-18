import requests
from sheets import *
from config import url_send_mensagem

"""
Esse é o arquivo mais extenso e difícil, onde eu trabalho os dados que recebi. Importo a url, requests para enviar e receber dados
E o sheets para manipular a planilha.
"""
class Bot: #Instancio a clase bot
    def __init__(self):#Inicio os valores que ela vai ter no futuro

        self.chat_id = None
        self.text = None
        self.first_name = None
        self.last_name = None
    def passando_dados(self, data):#Nessa parte é onde chega os dados em JSON
        #Pego o nome, o id do chat para responder
        mensagem = data['message']
        self.incoming_mensagem_text = ''
        self.incoming_mensagem_id = 0
        self.chat_id = mensagem['chat']['id']
        if 'text' in mensagem:
            self.incoming_mensagem_text = mensagem['text'].lower()
        elif 'new_chat_member' in mensagem:#Quando uma pessoa entra, não aparece como mensagem e sim como uma chave, então por isso é mais fácil procurar pela chave
            self.incoming_mensagem_text = 'novo membro'
        elif 'left_chat_member' in mensagem:
            self.incoming_mensagem_text = 'saiu'
        self.first_name = mensagem['from']['first_name']
        self.last_name = mensagem['from']['last_name']
        #Posso ajudar quem queira saber melhor esses dados, é muito dificil explicar sem mandar foto.

    def action(self):#Aqui é onde eu vejo a mensagem que veio e trato ela.
        """
        Vejo qual mensagem, faço if e defino qual vai ser a mensagem de saída(outgoing) e sempre executo a função para enviar a mensagem
        O success ali é uma bool para dar return no arquivo main e enviar para o Telegram que esse dado foi tratado e que ele pode descartar
        O telegram guarda os dados por 24 horas, e eles ficam esperando uma reposta. Usando webhooknão é possível ver as mensagens porém
        Com o metódo getWebhookInfo dá para saber quantas respostas estão pendentes.
        """
        
        success = None

        if self.incoming_mensagem_text == 'novo membro':
            self.outgoing_mensagem_text= "Seja bem-vindo {}! Se atente as regras e bons trades!".format(self.first_name)
            success=self.enviar_mensagem()

        if self.incoming_mensagem_text == '/rad':
            self.outgoing_mensagem_text = '🤙'
            success = self.enviar_mensagem()
        
        if self.incoming_mensagem_text == 'saiu':
            success=True
        
        if '/boleta' in self.incoming_mensagem_text:
            tem, linha = procura_nome("{} {}".format(self.first_name,self.last_name))
            if tem:
                altera_boleta(linha)
                self.outgoing_mensagem_text = 'Número de boletas atualizado para {} {} !'.format(self.first_name,self.last_name)
                success = self.enviar_mensagem()
            else:
                cria_linha(self.first_name,self.last_name)
                self.outgoing_mensagem_text = 'Parabéns por enviar sua primeira boleta, seja bem vindo a familía {} {} !'.format(self.first_name,self.last_name)
                success = self.enviar_mensagem()

        return success
    def enviar_mensagem(self):
        
        res = requests.get(url_send_mensagem.format(self.chat_id, self.outgoing_mensagem_text))#pego aquela url e formato ela como explicado antes

        return True if res.status_code == 200 else False#Dependendo do código que os servidores me retornam eu trato o 'return' como true ou false

    @staticmethod
    def init_webhook(url): #Esse é o cara que dá ao Telegram o link para mandar as informações
        requests.get(url)
