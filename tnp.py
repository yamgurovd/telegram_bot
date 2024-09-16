from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from src.credentional import BOT_TOKEN
from src.randomizers import randomizer_text, randomizer_person, randomizer_area
from aiogram.types import ContentType
from aiogram import F
from ai.handler_ai import output_
from ai.handler_ai_2 import output_2


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7217299582:AAFGFpvK_26l4-1Jjvopj1wg966OFKnPPfk'

API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def get_help(message: Message):
    await message.answer("Привет дорогой друг 🙌 \n"
                         "Для работы с ботом список доступных команд -  /help \n"
                         "Спасибо в тестировании бота 🙏 \n"
                         "Для обратной связи - @yamgurovd 😉")


@dp.message(Command(commands=["help"]))
async def get_help(message: Message):
    await message.answer("Список доступных команд: \n "
                         " /text_200 - Генерирует текст на анг(200 сим), \n"
                         " /ML_1 - ИИ модель взята с https://huggingface.co/EleutherAI/pythia-70m, \n"
                         " /fio_male - Генерирует ФИО мужское, \n"
                         " /fio_female - Генерирует ФИО женское, \n"
                         " /email - Генерирует email")


@dp.message(Command(commands=["text_200"]))
async def randomizer_text_(message: Message):
    await message.answer(f"{randomizer_text.generate_text(size_text=200)}")


@dp.message(Command(commands=["fio_male"]))
async def randomizer_text_(message: Message):
    await message.answer(f"Сгенерировано мужское ФИО: {randomizer_person.generate_last_name_male()} "
                         f"{randomizer_person.generate_first_name_male()} "
                         f"{randomizer_person.generate_middle_name_male()}")


@dp.message(Command(commands=["fio_female"]))
async def randomizer_text_(message: Message):
    await message.answer(f"Сгенерировано мужское ФИО: {randomizer_person.generate_last_name_female()} "
                         f"{randomizer_person.generate_first_name_female()} "
                         f"{randomizer_person.generate_middle_name_female()}")


@dp.message(Command(commands=["email"]))
async def randomizer_text_(message: Message):
    await message.answer(f"Сгенерирован адрес: {randomizer_area.generate_street_address_with_county()}")


@dp.message(Command(commands=["ML_1"]))
async def randomizer_text_(message: Message):
    await message.answer(output_())


# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)


@dp.message()
async def send_echo(message: types.Message):
    user_input = message.text
    print(user_input)
    response = output_2(textinput=user_input)
    print(response)
    await message.reply(text=response)


dp.message.register(get_help, Command(commands=["start"]))
dp.message.register(get_help, Command(commands=["help"]))
dp.message.register(randomizer_text_, Command(commands="text_200"))
dp.message.register(randomizer_text_, Command(commands="fio_male"))
dp.message.register(randomizer_text_, Command(commands="fio_female"))
dp.message.register(randomizer_text_, Command(commands="/email"))
dp.message.register(randomizer_text_, Command(commands=["ML_1"]))
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
