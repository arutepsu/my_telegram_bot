from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMIN_ID, bot
from Database.sql_commands import Database


class SurveyListState(StatesGroup):
    WaitingForSurveySelection = State()


async def list_surveys(message: types.Message):
    print(ADMIN_ID)
    print(message.from_user.id)
    if message.from_user.id == int(ADMIN_ID):
        db = Database()
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"Choose a survey id:\n"
                 f"1. Ideas\n"
                 f"2. Problems"
        )
        await SurveyListState.WaitingForSurveySelection.set()
    else:
        await message.answer("You are not authorized to access this command.")


async def get_survey_details(message: types.Message, state: FSMContext):
    if str(message.from_user.id) == ADMIN_ID:
        try:
            survey_id = int(message.text)
            db = Database()

            if survey_id == 1:
                ideas = db.get_ideas()

                for idea_tuple in ideas:
                    idea = idea_tuple[0]
                    await bot.send_message(
                        chat_id=message.from_user.id,
                        text=f"Idea: {idea}"
                    )

            elif survey_id == 2:
                problems = db.get_problems()

                for problem_tuple in problems:
                    problem = problem_tuple[0]
                    await bot.send_message(
                        chat_id=message.from_user.id,
                        text=f"Problem: {problem}"
                    )

            else:
                raise ValueError

        except (ValueError, TypeError):
            await message.answer("Invalid survey ID. Please enter a valid ID.")
        await state.finish()


def register_survey_list_handlers(dp: Dispatcher):

    dp.register_callback_query_handler(list_surveys,
                                       lambda call: call.data == "list_surveys")
    dp.register_message_handler(get_survey_details, state=SurveyListState.WaitingForSurveySelection)