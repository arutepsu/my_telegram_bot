from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    start_button = InlineKeyboardButton(
        "Start survey",
        callback_data="start_survey"
    )
    registration_button = InlineKeyboardButton(
        "Start Registration",
        callback_data="registration"
    )
    markup.add(start_button)
    markup.add(registration_button)
    return markup


async def survey_keyboard():
    markup = InlineKeyboardMarkup()
    choice_1_button = InlineKeyboardButton(
        "Choice_1",
        callback_data="choice_1"
    )
    choice_2_button = InlineKeyboardButton(
        "Choice_2",
        callback_data="choice_2"
    )
    choice_3_button = InlineKeyboardButton(
        "Choice_3",
        callback_data="choice_3"
    )
    markup.add(choice_1_button)
    markup.add(choice_2_button)
    markup.add(choice_3_button)
    return markup
