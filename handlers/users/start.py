import asyncpg.exceptions
import requests
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from database.connection import add_user
from database.models import Users
from keyboards.default.send_location import keyboard
from loader import dp, db, bot
from utils.misc.weather_api import get_current_weather_api


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    await add_user(user_id, full_name)
    await message.answer("Assalomu alaykum ob havo botga xush kelibsiz !")
    await message.answer("Shaxar nomini kiriting", reply_markup=keyboard)

# teacher in write weatherman
# @dp.message_handler(content_types='text')
# async def get_location(msg: types.Message):
#     result = await get_current_weather_api(msg.text)
#     await msg.answer(f"{result[1]}\n"
#                      f"UTC: {result[2]}\n"
#                      f"{msg.text.capitalize()} - {result[0]}\n")
#     print(result)





@dp.message_handler(content_types='text')
async def get_location(msg: types.Message):
    meteo = await get_current_weather_api(msg.text)
    await msg.answer(f"Country: {meteo['sys']['country']}\n"
                     f"City: {meteo['name']}\n"
                     f"harorat: {meteo['main']['feels_like']}\n"
                     f"bosim: {meteo['main']['pressure']}hPa\n"
                     f"namlik: {meteo['main']['humidity']}%\n"
                     f"havo holati: {meteo['weather'][0]['description']}")
    #
    # print(meteo)
    # print(meteo['main'])
    # print(meteo['weather'][0]['description'])