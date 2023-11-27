import sqlite3

import aiogram
from aiogram import types, Dispatcher
from config import bot
from const import USER_DATA_TEXT
from Database.sql_commands import Database, sql_queries
from Keyboards.inline_buttons import like_dislike_keyboard, my_profile_keyboard
import random
import re


async def my_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.sql_select_one_user_data(
        tg_id=call.from_user.id
    )
    print(profile)
    with open(profile["photo"], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=USER_DATA_TEXT.format(
                nickname=profile['nickname'],
                age=profile['age'],
                gender=profile['gender'],
                location=profile['location'],
                bio=profile['bio'],
            ),
            reply_markup=await my_profile_keyboard()
        )


async def random_profiles_call(call: types.CallbackQuery):
    print(call.message.caption)
    db = Database()
    profiles = db.filter_data(
        tg_id=call.from_user.id
    )
    if not profiles:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="There is no user_forms\n"
                 "or u liked all forms"
        )
        return
    print(profiles)
    random_profile = random.choice(profiles)
    with open(random_profile["photo"], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=USER_DATA_TEXT.format(
                nickname=random_profile['nickname'],
                age=random_profile['age'],
                gender=random_profile['gender'],
                location=random_profile['location'],
                bio=random_profile['bio'],
            ),
            reply_markup=await like_dislike_keyboard(
                owner_tg_id=random_profile['telegram_id']
            )
        )


async def like_detect_call(call: types.CallbackQuery):
    owner = re.sub("liked_profile_", "", call.data)
    db = Database()
    try:
        db.insert_sql_like(
            owner=owner,
            liker=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="You have liked this form before"
        )
    finally:
        await call.message.delete()
        await random_profiles_call(call=call)


def register_profile_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
    )
    dp.register_callback_query_handler(
        random_profiles_call,
        lambda call: call.data == "random_profiles"
    )
    dp.register_callback_query_handler(
        like_detect_call,
        lambda call: "liked_profile_" in call.data
    )

