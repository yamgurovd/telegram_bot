import requests
from src.credentional import BOT_TOKEN, API_URL
from src.randomizers import randomizer_text
from src import user_data

""""Пример запроса отправки сообщения пользователю GET/sendMessage

    URL запроса - https://api.telegram.org/bot<token>/sendMessage?chat_id=173901673&text=Привет, Mikhail!
    Method - GET 
    result - {
    "ok": true,
    "result": {
        "message_id": 1575,
        "from": {
            "id": 5424991242,
            "is_bot": true,
            "first_name": "New_name",
            "username": "VeryVeryVerySmart_bot"
        },
        "chat": {
            "id": 173901673,
            "first_name": "Mikhail",
            "last_name": "Kryzhanovskiy",
            "username": "kmsint",
            "type": "private"
        },
        "date": 1668981114,
        "text": "Привет, Mikhail!"
    }
}
"""


def get_sendMessage(size_text: int):
    """
    :param size_text: Размер текста, который необходимо отправить чат боту, используется для в библиотеке faker
    :return: Отправляет сгенерированный текст пользователю
    """
    text = randomizer_text.generate_text(size_text=size_text)

    return requests.get(f"{API_URL}{BOT_TOKEN}/sendMessage?chat_id={user_data.chat_id}&text={text}")


"""Раскомментировать код ниже"""
user = get_sendMessage(size_text=200)
#
print(f"URL запроса - {user.url}")
print(f"Method - {user.request}")
print(f"Response - {user.json()}")
