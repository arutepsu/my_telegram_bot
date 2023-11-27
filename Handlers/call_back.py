from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot
from Database.sql_commands import Database
from Keyboards.inline_buttons import survey_keyboard


async def start_survey_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Some Question",
        reply_markup=await survey_keyboard()
    )


async def choice_1_call(call: types.CallbackQuery):
    user_id = call.from_user.id
    response = "Choice 1"
    db = Database()
    db.insert_sql_callback(user_id, response)
    await bot.send_message(
        chat_id=user_id,
        text="Your answer (Choice 1) has been saved!"
    )


async def choice_2_call(call: types.CallbackQuery):
    user_id = call.from_user.id
    response = "Choice 2"
    db = Database()
    db.insert_sql_callback(user_id, response)
    await bot.send_message(
        chat_id=user_id,
        text="Your answer (Choice 2) has been saved!"
    )


async def choice_3_call(call: types.CallbackQuery):
    user_id = call.from_user.id
    response = "Choice 3"
    db = Database()
    db.insert_sql_callback(user_id, response)
    await bot.send_message(
        chat_id=user_id,
        text="Your answer (Choice 3) has been saved!"
    )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_survey_call,
                                       lambda call: call.data == "start_survey")
    dp.register_callback_query_handler(choice_1_call,
                                       lambda call: call.data == "choice_1")
    dp.register_callback_query_handler(choice_2_call,
                                       lambda call: call.data == "choice_2")
    dp.register_callback_query_handler(choice_3_call,
                                       lambda call: call.data == "choice_3")
