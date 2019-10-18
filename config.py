import requests
import json

"""
Essa parte pode ser feita sem importação nenhuma, porém o ngrok possui uma api e assim fica mais fácil saber qual será o site externo
Então toda vez que eu inicio o bot, não é necessário ficar pegando manualmente o site no qual será definido como webhook.
"""

ngrok_site_request = requests.get('http://localhost:4040/api/tunnels/command_line')
ngrok_site_final = json.loads(ngrok_site_request.text)['public_url']#usando a API para pegar o site externo que foi gerado para mim.
url_base = 'https://api.telegram.org/bot<TOKEN>' #Essa é a URL base para qualquer update ou metodo do Telegram, precisando apenas substituir pelo seu token.
definindo_webhook = '{}/setWebhook?url={}/webhook'.format(url_base,ngrok_site_final) #variavel que monta o link para definir o webhook
url_send_mensagem = url_base+'/sendMessage?chat_id={}&text={}' #URL para enviar mensagem, deixo os {} pois assim eu consigo mudar vistoo que apenas os id's variam e o texto também

"""
Aqui está a explicação de como funciona a aplicação, a maquina faz todo o processamento e usa o flask para abrir as portas e enviar para a url local
O ngrok usa a mesma porta, pega a url local e transforma ela em externa, permitindo a transferencia de dados para o Telegram e a recepção também
"""