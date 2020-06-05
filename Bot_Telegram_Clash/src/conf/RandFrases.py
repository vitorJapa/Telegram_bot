import requests
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import BASE_API_URL, TELEGRAM_TOKEN

from random import randint
#retorna uma frase aleatoria das cadastradas
url ="https://api.telegram.org/bot1199430211:AAFkdGBLmMk7PS2K88Zq8E2oekJLCdQtak0/sendmessage"

def frases():
    random = randint(1,4)
    if random == 1:
        #for n in random:
        frase = 'MAINHA NÃO DEIXA'

    elif random == 2:
        frase = 'VOU ABRIR PK'

    elif random == 3:
        frase = 'PEIDEI'

    elif random == 4:
        frase = 'EU SO QUERIA ALMOCAR'

    else:
        frase = 'SEM FRASE PRA VC HOJE'
    print(frase)

    data ={"chat_id":-306508965, "text":frase}
    response = requests.post(url, data=data)

    return true
