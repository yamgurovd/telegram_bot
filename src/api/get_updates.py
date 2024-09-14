import requests

from src.credentional import API_URL, BOT_TOKEN

"""Получить информацию сообщений присланных из телеграм бота"""


def get_getUpdates(offset: int = -2):
    """
    :return: Данные о пользователе и данных при взаимодействии с чат ботом
    """

    updates = requests.get(f"{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}")

    return updates
