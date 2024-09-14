import requests
from src.credentional import BOT_TOKEN, API_URL

""""Пример запроса получения информации пользователя GET/getUpdates

    URL запроса - https://api.telegram.org/bot<token>/getUpdates
    Method - GET 
    response = {
    "ok": true,
    "result": [
        {
            "update_id": 396710491,
            "message": {
                "message_id": 1573,
                "from": {
                    "id": 173901673,
                    "is_bot": false,
                    "first_name": "Mikhail",
                    "last_name": "Kryzhanovskiy",
                    "username": "kmsint",
                    "language_code": "ru"
                },
                "chat": {
                    "id": 173901673,
                    "first_name": "Mikhail",
                    "last_name": "Kryzhanovskiy",
                    "username": "kmsint",
                    "type": "private"
                },
                "date": 1668979407,
                "text": "/start",
                "entities": [
                    {
                        "offset": 0,
                        "length": 6,
                        "type": "bot_command"
                    }
                ]
            }
        }
    ]
}

Если вы в ближайшее время никак с вашим ботом не взаимодействовали - ответ будет вида:
{'ok': True, 'result': []}

"""


def get_getUpdates():
    """
    :return: Данные о пользователе и данных при взаимодействии с чат ботом
    """
    offset = -2
    return requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}')


"""Раскомментировать код ниже
    Перед запуском функции get_getUpdates необходимо отправить сообщение в телеграм боте
"""

# user = get_getUpdates()
#
# print(f"URL запроса - {user.url}")
# print(f"Method - {user.request}")
# print(f"Response - {user.json()}")
