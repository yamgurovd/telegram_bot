@dp.message()
async def send_echo(message: types.Message):
    user_input = message.text
    is_latin = contains_latin(text=user_input)

    if is_latin:
        response = output_2(textinput=user_input)
        await message.reply(text=response)
    else:

        translator = Translator()

        text = output_2(textinput=user_input)
        translated = translator.translate(text=text, src='ru', dest='en')

        question_AI = output_2(textinput=translated)

        translated_convert = translator.translate(text=question_AI, dest='ru')

        await message.reply(text=translated_convert)
