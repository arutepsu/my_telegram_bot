import sqlite3

from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link

from config import bot
from Database.sql_commands import Database
from Keyboards.inline_buttons import start_keyboard


async def start_button(message: types.Message):
    print(message)
    db = Database()

    print(message.get_full_command())
    command = message.get_full_command()
    if command[1] != "":
        link = await _create_link(link_type="start", payload=command[1])
        user = db.sql_select_user_by_link(
            link=link
        )
        print(user)

        if user['tg_id'] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text="This is your link!"
            )
            return
        else:
            try:
                db.sql_update_balance(
                    tg_id=user['tg_id']
                )
                db.sql_insert_referral(
                    owner=user['tg_id'],
                    referral=message.from_user.id
                )
                db.sql_insert_balance_query(
                    owner=user['tg_id'],
                    amount=0
                )
            except sqlite3.IntegrityError:
                pass

    db.insert_sql_users(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        firstname=message.from_user.first_name,
        lastname=message.from_user.last_name,
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Hi. I am Heimdallr and I check if there are any curse words in chat. "
             "Don't curse or you go in Valhalla.",
        reply_markup=await start_keyboard()
    )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])
