# Тестовый запуск метода /sendMessage

import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7217299582:AAFGFpvK_26l4-1Jjvopj1wg966OFKnPPfk'

offset = -2
counter = 0
chat_id = int

while True:

    # print(f"Attempt = {counter}")  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            print("====================== ЛОГИ ===================")
            print("Медоl GET/sendMessage")
            print(f"Время оправки сообщения {time.ctime()}")

            offset = result['update_id']
            print(f"message_id: {offset}")

            chat_id = result['message']['from']['id']
            print(f"chat_id: {chat_id}")

            first_name = result['message']['from']['first_name']
            print(f"first_name: {first_name}")

            last_name = result.get('message').get('from').get('last_name', 'There is no last_name')
            print(f"last_name: {last_name}")

            username = result.get('message').get('from').get('username', 'There is no username')
            print(f"username: {username}")

            ink = "═══════❖═══════"

            text = f"Привет {first_name} {last_name} спасибо, что помогаешь в тестировании бота yamgurovd 😇"
            text_2 = f"Пока умею только это"
            text_3 = "Но это не точно 😈 😉 "

            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ink}')

            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}')

            time.sleep(1)
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text_2}')

            time.sleep(7)
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text_3}')

            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ink}')

            time.sleep(2)
            counter += 1
