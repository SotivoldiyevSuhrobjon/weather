from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
btn = KeyboardButton(text="📍 Joylashuv yuborish",request_location=True)
keyboard.add(btn)