from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from src.credentional import BOT_TOKEN
from src.randomizers import randomizer_text, randomizer_person, randomizer_area
from aiogram.types import ContentType
from aiogram import F
# from ai.handler_ai import output_
from ai.handler_ai_2 import output_2
from src.helper import checker
from googletrans import Translator, LANGUAGES
from aiogram import types

translator = Translator()

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7217299582:AAFGFpvK_26l4-1Jjvopj1wg966OFKnPPfk'

API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def get_start(message: Message):
    await message.answer("Привет дорогой друг 🙌 \n"
                         "Для работы с ботом список доступных команд -  /help \n"
                         "Спасибо в тестировании бота 🙏 \n"
                         "Для обратной связи - @yamgurovd 😉")


@dp.message(Command(commands=["help"]))
async def get_help(message: Message):
    await message.answer("Список доступных команд: \n "
                         "/text_200 - Генерирует текст на анг(200 сим), \n"
                         "/fio_male - Генерирует ФИО мужское, \n"
                         "/fio_female - Генерирует ФИО женское, \n"
                         "/email - Генерирует email, \n"
                         "/en_ru text - Переводит текст с англ на рус - нужно вводить команда + текст\n"
                         "/ru_en text - Переводит текст с рус на англ - нужно вводить команда + текст\n"
                         "Общение с ИИ моделью на англ и рус - Пример: как дела?/ how are you?\n"
                         "ИИ модель взята с https://huggingface.co/EleutherAI/pythia-70m, ")


@dp.message(Command(commands=["text_200"]))
async def random_text_200(message: Message):
    await message.answer(f"{randomizer_text.generate_text(size_text=200)}")


@dp.message(Command(commands=["fio_male"]))
async def random_fio_male(message: Message):
    await message.answer(f"Сгенерировано мужское ФИО: {randomizer_person.generate_last_name_male()} "
                         f"{randomizer_person.generate_first_name_male()} "
                         f"{randomizer_person.generate_middle_name_male()}")


@dp.message(Command(commands=["fio_female"]))
async def random_fio_female(message: Message):
    await message.answer(f"Сгенерировано женское ФИО: {randomizer_person.generate_last_name_female()} "
                         f"{randomizer_person.generate_first_name_female()} "
                         f"{randomizer_person.generate_middle_name_female()}")


@dp.message(Command(commands=["email"]))
async def random_email(message: Message):
    await message.answer(f"Сгенерирован адрес: {randomizer_area.generate_street_address_with_county()}")


@dp.message(Command(commands=["en_ru"]))
async def translate_to_ru(message: Message):
    text = message.text
    translated = translator.translate(text=text[len("/en_ru"):], dest='ru')
    await message.answer(f"Перевод текста на русский: {translated.text}")


#
#
@dp.message(Command(commands=["ru_en"]))
async def translate_to_en(message: Message):
    text = message.text
    translated = translator.translate(text=text[len("/ru_en"):], src="ru", dest='en')
    await message.answer(f"Перевод текста на английский: {translated.text}")


@dp.message()
async def send_echo(message: types.Message):
    user_input = message.text
    is_latin = checker.contains_latin(text=user_input)

    if is_latin:
        response = output_2(textinput=user_input)
        await message.reply(text=response)
    else:

        translator = Translator()

        text = output_2(textinput=user_input)
        translated = translator.translate(text=text, src='ru', dest='en')

        question_AI = output_2(textinput=str(translated))

        translated_convert = translator.translate(text=question_AI, dest='ru')

        await message.reply(text=translated_convert.text)


dp.message.register(get_start, Command(commands=["start"]))
dp.message.register(get_help, Command(commands=["help"]))
dp.message.register(random_text_200, Command(commands="text_200"))
dp.message.register(random_fio_male, Command(commands="fio_male"))
dp.message.register(random_fio_female, Command(commands="fio_female"))
dp.message.register(random_email, Command(commands="email"))
dp.message.register(translate_to_ru, Command(commands="en_ru"))
dp.message.register(translate_to_en, Command(commands="ru_en"))
# dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
