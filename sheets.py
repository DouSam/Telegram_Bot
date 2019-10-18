import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import pprint
"""
Essa área é um adendo, uso o google sheets para armazenar os dados que colote no grupo do telegram, assim todos os adms conseguem ter acesso
O pprint é extremamente útil pois ao longo do tempo a planilha vai ficando grande e é necessário printar mais bonito para fácil identificação
Dos dados. A váriavel scope está descrita no próprio API, não entendi ao certo pq é usada porém é necessária para o funcionamento e acesso das
Planilhas.
"""

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",scope)#Abrimos as credencias do arquivo.
client = gspread.authorize(creds)#Dessa forma fazemos o 'login', com o arquivo que pegamos no console de API Google

"""
Essas duas variaveis são usadas varias vezes no código por isso coloquei elas antes. Essa é para abrir a planilha, pesquisamos ela pelo nome 
E definimos a área de trabalho na qual ela está, no meu caso sempre está no sheet1
#sheet = client.open("boleta").sheet1  

Essa é para acessar os dados da planilha, ele te gera uma lista e dentro da lista um dicionário, o indice zero é a segunda linha pois na primeira
Definimos o que terá na coluna e então no dicionário estará na chave o primeiro item da coluna(por ordem alfabetica). Vou trazer um exemplo
Primeira linha, primeira e segunda coluna está escrito respectivamente : Nome e Idade. na segunda linha está primeira coluna: Douglas segunda:18
Quando damos o print, ele retorna uma lista com len = 1 e dentro um dicionario com a chave 'Idade':18 e 'Nome': 'Douglas'
#data = sheet.get_all_records() 

Eu não chamo apenas no começo pois ela atualiza muito e se eu não chamasse a cada função eu estaria sempre pegando uma planilha na qual os dados 
Já podem ter mudado pelo prórpio bot.
""" 

def procura_nome(nome):#Essa é pra procurar o nome de uma pessoa na planilha.
    sheet = client.open("boleta").sheet1  
    data = sheet.get_all_records() 
    #Defino a linha zero a primeira que vou procurar e o 'tem' como false, váriaveis que irei retornar
    linha = 0
    tem=False
    while linha < len(data):#While para pesquisar linha a linha.
        if nome in data[linha]['Nome']:
            tem = True
            break
        else:
            linha= linha+1
    return tem, linha+2 #Como inicia no zero na programação mas não na planilha, eu tenho que adicionar 1 e como a primeira linha não conta eu tenho que adicionar mais 1
    #Totalizando 2 e retorno se o nome está na planilha e se ele está eu retorno a linha.
    
def altera_boleta(linha):#Essa é específica para o projeto, como disse eu contabilizo as boletas, logo se o nome da pessoa já está na planilha eu apenas somo a nova boleta.
    sheet = client.open("boleta").sheet1  
    data = sheet.get_all_records()  

    numero_boletas_ant = sheet.cell(linha,2).value#Pego o valor de uma célula exata, dando a linha e coluna
    numero_boletas_ant_int = int(numero_boletas_ant)#Como vou somar, transformo o valor em int
    novo_numero = numero_boletas_ant_int + 1
    atualiza_boleta = sheet.update_cell(linha,2,novo_numero)#Após a soma eu atualizo a celula, dando a localização e o que irá mudar.
    
def cria_linha(nome,sobrenome):#Essa é para caso o nome da pessoa não esteja lá
    sheet = client.open("boleta").sheet1  
    data = sheet.get_all_records()  

    numero_linhas= len(data)+2#Pego qual foi a última linha preenchida e adiciono mais um para colocar os dados nela.
    novo_nome= sheet.update_cell(numero_linhas,1,'{} {}'.format(nome,sobrenome))#Mudo o nome dando a linha e coluna do mesmo jeito.
    nova_boleta= sheet.update_cell(numero_linhas,2,1)

