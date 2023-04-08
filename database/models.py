from peewee import *
# from data.config import DB_HOST,DB_USER,DB_NAME,DB_PASS


db = SqliteDatabase("bot.db")


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    user_id = BigIntegerField(primary_key=True)
    username = CharField(max_length=200, null=True)

    class Meta:
        db_name = 'users'
