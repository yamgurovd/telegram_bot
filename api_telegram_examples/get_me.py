import requests
from src.credentional import BOT_TOKEN, API_URL

""""Пример запроса получения информации пользователя GET/getMe

    URL запроса - https://api.telegram.org/bot<TOKEN>/getMe
    Method - GET 
    response - {
        "ok": true,
        "result": {
            "id": 5424991242,
            "is_bot": true,
            "first_name": "New_name",
            "username": "VeryVeryVerySmart_bot",
            "can_join_groups": true,
            "can_read_all_group_messages": false,
            "supports_inline_queries": true
        }
    }
"""


def get_getMe():
    return requests.get(f"{API_URL}{BOT_TOKEN}/getMe")


"""Раскомментировать код ниже"""
# user = get_getMe()
#
# print(f"URL запроса - {user.url}")
# print(f"Method - {user.request}")
# print(f"Response - {user.json()}")
