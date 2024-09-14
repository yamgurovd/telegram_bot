import requests
from src.credentional import BOT_TOKEN, API_URL
from src.randomizers import randomizer_text
from src import user_data


def get_sendMessage(size_text: int):
    """
    :param size_text: Размер текста, который необходимо отправить чат боту, используется для в библиотеке faker
    :return: Отправляет сгенерированный текст пользователю
    """
    text = randomizer_text.generate_text(size_text=size_text)

    return requests.get(f"{API_URL}{BOT_TOKEN}/sendMessage?chat_id={user_data.chat_id}&text={text}")