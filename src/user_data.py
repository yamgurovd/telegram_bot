import requests
from src.credentional import API_URL, BOT_TOKEN


def get_user_info():
    """
    :return: Данные о пользователе и данных при взаимодействии с чат ботом
    """
    offset = -2

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    return updates


user = get_user_info()

for param in user["result"]:
    offset = param["update_id"]
    first_name = param['message']["from"].get("first_name", "There is no first_name")
    last_name = param['message']["from"].get("last_name", "There is no last_name")
    username = param['message']["from"].get("username", "There is no username")
    chat_id = param['message']['from'].get("id", "There is no chat_id")

offset: int = offset
first_name: str = first_name
last_name: str = last_name
username: str = username
chat_id: str = chat_id
