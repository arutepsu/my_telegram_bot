from aiogram import types, Dispatcher
from config import bot
from Database.sql_commands import Database
from Keyboards.inline_buttons import start_keyboard


async def start_button(message: types.Message):
    print(message)
    db = Database()
    db.insert_sql_users(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        firstname=message.from_user.first_name,
        lastname=message.from_user.last_name,
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text="You are in DB now!",
        reply_markup=await start_keyboard()
    )

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])
