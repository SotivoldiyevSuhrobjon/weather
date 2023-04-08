from data.config import ADMINS
from .models import *
from loader import bot,db


async def add_user(user_id: int, username: str):
    with db:
        if not Users.select().where(Users.user_id == user_id).exists():
            Users.create(user_id=user_id, username=username)
            count = Users.select().count()
            msg = f"{username} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor"
            for admin in ADMINS:
                await bot.send_message(admin,msg)

