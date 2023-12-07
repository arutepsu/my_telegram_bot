
from aiogram import types, Dispatcher
from config import bot
from Database.sql_commands import Database
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class SurveyStates(StatesGroup):
    idea = State()
    problems = State()


async def survey_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Which ideas do you can suggest to improve me?"
    )
    await SurveyStates.idea.set()


async def load_idea(message: types.Message,
                    state: FSMContext):
    async with state.proxy() as data:
        data['idea'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Which problems did you encounter using me?"
    )
    # await SurveyStates.problems.set()
    await SurveyStates.next()


async def load_problems(message: types.Message,
                    state: FSMContext):
    async with state.proxy() as data:
        data['problems'] = message.text
        print(data)
        db = Database()
        db.sql_insert_survey_query(data['idea'], data['problems'], message.from_user.id)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Thank you for your feedback!"
    )
    await state.finish()



def register_survey_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        survey_start,
        lambda call: call.data == "survey"
    )
    dp.register_message_handler(
        load_idea,
        state=SurveyStates.idea,
        content_types=['text']
    )
    dp.register_message_handler(
        load_problems,
        state=SurveyStates.problems,
        content_types=['text']
    )
