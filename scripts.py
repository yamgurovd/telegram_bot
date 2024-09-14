# Тестовый запуск метода /sendMessage
from src.credentional import API_URL, BOT_TOKEN
from src import user_data
from src.api.get_send_message import get_sendMessage

counter = 0

while True:
    send_message = get_sendMessage(size_text=200)
    counter += 1





