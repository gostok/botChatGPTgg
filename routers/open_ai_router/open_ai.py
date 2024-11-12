from aiogram import Router, types, F
import os
from openai import OpenAI

from routers.menu_router.menu_kb import menu_kb

open_ai_router = Router()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),
                base_url=os.getenv("BASE_URL_OPENAI"))


@open_ai_router.message(F.text)
async def chat_with_gpt(message: types.Message):
    user_message = message.text

    try:
        # Отправка запроса к API OpenAI
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",  # Выберите модель, которую вы хотите использовать
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        # Получение ответа от модели
        bot_reply = response.choices[0].message.content

        # Отправка ответа пользователю
        await message.answer(bot_reply, reply_markup=menu_kb())
    except Exception as e:
        await message.answer("Произошла ошибка при обработке вашего запроса. Пожалуйста, попробуйте снова.",
                             reply_markup=menu_kb())
        print(f"Error: {e}")