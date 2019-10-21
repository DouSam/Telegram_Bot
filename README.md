# Telegram_Bot v1.1
Um bot feito para o telegram para um grupo de trade, usando API Telegram e Google Sheets.
Está mais explicado nos próprios arquivos dele, caso você queria testar é só instalar as bibliotecas no seu computador e colocar seu TOKEN, caso queira um tutorial mais detalhado pode me marcar ou mandar mensagem, tanto para a API do Telegram quanto para a API do Google Sheets.

Atualização v1.1
No main.py, adicionei um sleep para evitar conflitos na api do google, quando o bot consultava muitas vezes o sheets, o programa dava alguns erros por multiplos acessos.
No bot.py, foi adicionado um sistema pra responder a mensagem, assim ele notifica a pessoa, um bloco para ler as legendas das imagens que são enviadas. Modificada a parte na qual pegava o sobrenome da pessoa pois a mesma poderia optar por não colocar sobrenome, mais funções como enviar uma sugestao e salvar em txt.

Ps: Boleta é uma especie de conta que mostra o quanto de acertos uma pessoa teve em um trade.
