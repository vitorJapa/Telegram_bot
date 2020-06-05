import requests
from random import randint

urlphoto ='https://api.telegram.org/bot1199430211:AAFkdGBLmMk7PS2K88Zq8E2oekJLCdQtak0/sendphoto?chat_id='

def foto(chat_id):
    random = randint(1,13)
    if random == 1: #brazzers
        foto = 'AgACAgEAAxkBAAIDul7ahvY16ZCERNYzssxLIChYW04gAAJXqDEbWVvZRimW_dY1iPq18qISMAAEAQADAgADbQADKdkAAhoE'

    elif random == 2: #dida em 2020
        foto = 'AgACAgEAAxkBAAIDs17agXdGT3G3VGqW05xy2_7QNj3AAAJRqDEbWVvZRrqTzR9h7ub4M95uBgAEAQADAgADbQADt3QCAAEaBA'

    elif random == 3: #shanks baleia
        foto = 'AgACAgEAAxkBAAIDtV7ahZT1gm618ezKhHhjSzdfgcVYAAJSqDEbWVvZRmi64t-kVPIuuMBuBgAEAQADAgADbQADdgYDAAEaBA'

    elif random == 4: #dida surfista
        foto = 'AgACAgEAAxkBAAIDtl7ahZRcgb_9CM2DUapX-OxA9G9hAAJTqDEbWVvZRty0b-N73DmFuvdrBgAEAQADAgADbQADfB8EAAEaBA'

    elif random == 5: #dida vayne
        foto = 'AgACAgEAAxkBAAIDt17ahZR8yRwjKxZMSkBXlQN1LW-lAAJUqDEbWVvZRmfs9pJ6jFMfhO3tSBcAAwEAAwIAA20AA4I3AAIaBA'

    elif random == 6: #dida chat solteiro
        foto = 'AgACAgEAAxkBAAIDuF7ahvZXZiFBlFQytP1hG0yFO9xFAAJVqDEbWVvZRtYqh9NUFunL-rluBgAEAQADAgADbQADDRMDAAEaBA'

    elif random == 7: #dida final msn
        foto = 'AgACAgEAAxkBAAIDuV7ahvZD51xVsVres683G7wggvMdAAJWqDEbWVvZRvq-MlJxSsOVBasSMAAEAQADAgADbQAD79sAAhoE'

    elif random == 8: #dida na chuva
        foto = 'AgACAgEAAxkBAAID5F7ar7MSzHycKQ5rYc8gd-gOpDUpAAJuqDEbWVvZRtetoGJ6aTAlL7huBgAEAQADAgADbQAD4xYDAAEaBA'

    elif random == 9: #dida mundo
        foto = 'AgACAgEAAxkBAAID5V7ar7MdIMBO_pcj7oBfrCNQuX9YAAJvqDEbWVvZRme6EOTgBMGlVOFuBgAEAQADAgADbQAD-nQCAAEaBA'

    elif random == 10: #dida dos namorados
        foto = 'AgACAgEAAxkBAAID5l7ar7Re5Rq6cdwIVi02NmQHcX4LAAJwqDEbWVvZRsZuV4nG3SPjCagSMAAEAQADAgADbQAD690AAhoE'

    elif random == 11: #role panela
        foto = 'AgACAgEAAxkBAAID517ar7WfwdWMo24DpoeJxFy0ljffAAJxqDEbWVvZRkWhxNXmT2zPrNVuBgAEAQADAgADbQAD7nUCAAEaBA'

    elif random == 12: #role panela metro
        foto = 'AgACAgEAAxkBAAID6F7ar7Vk3pxUCXaRHb5hBn-xzIE9AAJyqDEbWVvZRnv1Uah4pktwSeFuBgAEAQADAgADbQADwngCAAEaBA'

    elif random == 13: #dida vampirao
        foto = 'AgACAgEAAxkBAAID6V7ar7ZJdIyKVbfICyJkX388wM4hAAJzqDEbWVvZRrvbBnhYh4z-Bd9uBgAEAQADAgADbQADinoCAAEaBA'

    fullurl = "%s%s&photo=%s"%(urlphoto,chat_id,foto)
    response = requests.post(fullurl)
    print(fullurl)
    return True
