from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import BASE_API_URL, TELEGRAM_TOKEN
import requests
from Funcao.aert import foto
from random import randint

url ="https://api.telegram.org/bot1199430211:AAFkdGBLmMk7PS2K88Zq8E2oekJLCdQtak0/sendmessage"


def start(bot, update):
    response_message = 'Bem vindo ao Bot do Didao de Maceio.\n Segue alguns comandos registrados:\n /frases --> para uma frase minha \n/photo --> para uma linda foto'
    bot.send_message(chat_id=update.message.chat_id, text=response_message)

def support(bot, update):
    response_message = "Comandos uteis \n /frases \n /fotos"
    print(response_message)
    bot.send_message(chat_id=update.message.chat_id, text=response_message)

def frases(bot, update):
    print('comeco da chamada')
    random = randint(1,18)
    if random == 1:
        #for n in random:
        frase = 'MAINHA NÃO DEIXA'

    elif random == 2:
        frase = 'VOU ABRIR PK'

    elif random == 3:
        frase = 'Fim de mes eh triste, saudades do meu bb($$)'

    elif random == 4:
        frase = 'EU SO QUERIA ALMOCAR'

    elif random == 5:
        frase = 'Que saudade do almoço da sexta feira santa'

    elif random == 6:
        frase = 'Eu SO queria sexta feira...'

    elif random == 7:
        frase = 'Voces malham?'

    elif random == 8:
        frase = 'Olhe daniel, você não ta ajudando...'

    elif random == 9:
        frase = '#digaNaoAoMagrismo'

    elif random == 10:
        frase = 'As mulheres que amo, deixo-as livres para partir. Se ficarem eu conquistei. Se não ficarem, pelo menos eu comi.'

    elif random == 11:
        frase = '#VO PICKA NUNU SUPORT'

    elif random == 12:
        frase = 'MEU MALPITAO BATE NO RENEK DO DAN'

    elif random == 13:
        frase = 'DIDAO TOPLANER DA APAIN'

    elif random == 14:
        frase = 'Eu vou almocar, só deixa eu terminar de almocar'

    elif random == 15:
        frase = 'fase de crescimento é muito complicada mesmo \njá quero comer de novo'

    elif random == 16:
        frase = 'EU SOU TODAS AS LANES'

    elif random == 17:
        frase = 'MEU NICK EH 99G BRITNEY'

    else:
        frase = 'SEM FRASE PRA VC HOJE'
    print(frase)

    data ={"chat_id":update.message.chat_id, "text":frase}
    response = requests.post(url, data=data)
    return True


def photo(bot, update):
    foto(update.message.chat_id)
    return True


def unknown(bot, update):
    response_message = 'Comando não registrado'
    print(response_message)
    bot.send_message(chat_id=update.message.chat_id, text=response_message)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(token=TELEGRAM_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("frases", frases))
    dispatcher.add_handler(CommandHandler("photo", photo))
    dispatcher.add_handler(CommandHandler('support', support))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == "__main__":
    main()
