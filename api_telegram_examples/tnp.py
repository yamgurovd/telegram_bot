from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from src.credentional import BOT_TOKEN
from src.randomizers import randomizer_text
from aiogram.types import ContentType
from aiogram import F

API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["randomizer_text_200"]))
async def randomizer_text_(message: Message):
    await message.answer(f"{randomizer_text.generate_text(size_text=200)}")

@dp.message(Command(commands=["help"]))
async def get_help(message: Message):
    await message.answer("список доступных команд: \n /randomizer_text_200, /cotomizer")


@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)




# ...

# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)


dp.message.register(randomizer_text_, Command(commands="randomizer_text"))
dp.message.register(get_help, Command(commands=["help"]))
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)
