from aiogram import types, Dispatcher
from Database.sql_commands import Database
from config import bot, ADMIN_ID, dp
from Keyboards.inline_buttons import admin_keyboard, private_message_keyboard, ban_keyboard, survey_list_keyboard
from const import WARNING_TEXT


async def admin_call(message: types.Message):
    print(ADMIN_ID)
    print(message.from_user.id)
    if message.from_user.id == int(ADMIN_ID):
        await message.delete()
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Hello Master 🐲 \n "
                 "What would you like to do?",
            reply_markup=await admin_keyboard()
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="U r not my master 🤬"
        )


async def survey_call(message: types.Message):
    print(ADMIN_ID)
    print(message.from_user.id)
    if message.from_user.id == int(ADMIN_ID):
        await message.delete()
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Hello Admin!🐲 \n "
                 "Wanna check survey list?",
            reply_markup=await survey_list_keyboard()
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="U r not my master 🤬"
        )


async def all_profiles_data(call: types.CallbackQuery):
    db = Database()
    data = db.sql_select_all_tg_users()
    if data:
        for user in data:
            link = f"https://t.me/{user[2]}"
            await bot.send_message(
                chat_id=call.from_user.id,
                text=f"Telegram_id: {user[1]}\n"
                     f"Username: {user[2]} \n"
                     f"First_name: {user[3]}, Last_name: {user[4]}\n"
                     f"Reference_link: {user[5]}",
                reply_markup=await private_message_keyboard(link)
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="There are no users"
        )


async def potential_ban(call: types.CallbackQuery):
    global nickname
    db = Database()
    data = db.select_potential_ban_users()
    user_data = db.sql_select_all_tg_users()
    if data:
        for user in data:
            for one_user_data in user_data:
                link = f"https://t.me/{one_user_data[2]}"
                if user[1] == one_user_data[1]:
                    nickname = one_user_data[2]
                    break
                else:
                    nickname = None
            await bot.send_message(
                chat_id=call.from_user.id,
                text=f"Username: {nickname}\n"
                     f"Ban count: {user[2]} \n",
                reply_markup=await ban_keyboard(link, user[1])

            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="There are no potential ban users"
        )


async def warning_message(call: types.CallbackQuery):
    user_id_to_warn = int(call.data.split("_")[-1])
    if call.data.startswith(f"warning_message_{user_id_to_warn}"):
        db = Database()
        count_result = db.select_count_ban_user(user_id_to_warn)
        warning_count = count_result[0] if count_result else 0
        await bot.send_message(
            chat_id=user_id_to_warn,
            text=WARNING_TEXT.format(warning_count)
        )


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(survey_call,
                                lambda word: "sur" in word.text)
    dp.register_message_handler(admin_call,
                                lambda word: "dorei" in word.text)
    dp.register_callback_query_handler(all_profiles_data,
                                       lambda call: call.data == "all_users")
    dp.register_callback_query_handler(potential_ban,
                                       lambda call: call.data == "ban_data")
    dp.register_callback_query_handler(
        warning_message,
        lambda call: call.data.startswith("warning_message") and call.data.split('_')[-1].isdigit()
    )
