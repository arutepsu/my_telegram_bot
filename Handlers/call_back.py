from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot
from Database.sql_commands import Database
from Keyboards.inline_buttons import survey_keyboard, repeat_survey


async def start_survey_call(call: types.CallbackQuery):
    db = Database()
    row_count = db.check_callback(call.from_user.id)
    if row_count:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="The survey is already completed",
            reply_markup=await repeat_survey()
        )
    else:
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


async def repeat_survey_call(call: types.CallbackQuery):
    db = Database()
    db.delete_data(call.from_user.id)
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Your previous survey data has been deleted. You can start the survey again.",
        reply_markup=await survey_keyboard()
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
    dp.register_callback_query_handler(repeat_survey_call,
                                       lambda call: call.data == "repeat_survey")
