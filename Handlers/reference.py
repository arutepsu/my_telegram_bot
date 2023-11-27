from aiogram import types, Dispatcher
from config import bot
from Database.sql_commands import Database
from const import REFERENCE_MENU_TEXT
from aiogram.utils.deep_linking import _create_link
import binascii
import os


async def reference_users_call(call: types.CallbackQuery):
    db = Database()
    referral_users = db.sql_select_referral_users(tg_id=call.from_user.id)
    if referral_users:
        for user in referral_users:
            referral_telegram_id = user[1]
            await bot.send_message(
                chat_id=call.from_user.id,
                text=f"Referral user ID: {referral_telegram_id}"
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="You dont have any referral users!"
        )


async def reference_link_call(call: types.CallbackQuery):
    db = Database()
    user = db.sql_select_user_link(
        tg_id=call.from_user.id
    )
    print(user)
    if not user['link']:
        token = binascii.hexlify(os.urandom(8)).decode()
        link = await _create_link(link_type="start", payload=token)
        db.sql_update_reference_link(
            link=link,
            owner=call.from_user.id
        )
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Your link: {link}"
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Your link: {user['link']}",
        )


def register_reference_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(reference_link_call,
                                       lambda call: call.data == "reference_link")
    dp.register_callback_query_handler(reference_users_call,
                                       lambda call: call.data == "reference_list")
