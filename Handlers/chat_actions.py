import sqlite3

from aiogram import types, Dispatcher
from config import bot
from Database.sql_commands import Database
from profanity_check import predict, predict_prob


async def chat_messages(message: types.Message):
    db = Database()
    print(message)
    if message.chat.id == -1002038402284:
        ban_word_predict_prob = predict_prob([message.text])
        if ban_word_predict_prob > 0.1:
            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=message.message_id
            )
            user = db.select_sql_ban_user(
                telegram_id=message.from_user.id
            )
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"Deleted message from user {message.from_user.first_name}\n"
                     f"Please be chill!\n"
                     f"If you get this message more then 3 times"
                     f" you will go to Valhalla"
            )
            print(user)
            count = None
            try:
                count = user['count']
            except TypeError:
                pass
            if not user:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"{message.from_user.first_name} soon you will go to Valhalla!")
                db.insert_sql_ban_user(
                    telegram_id=message.from_user.id
                )
            elif count >= 3:
                # await bot.ban_chat_member(
                #     chat_id=message.chat.id,
                #     user_id=message.from_user.id,
                # )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"{message.from_user.first_name} went to Valhalla"
                )
            elif user:
                db.update_sql_ban_user_count(
                    telegram_id=message.from_user.id

                )
    else:
        await message.reply(
            text="Don't get such command!"
        )


def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_messages)
