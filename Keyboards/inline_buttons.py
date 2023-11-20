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
    my_profile_button = InlineKeyboardButton(
        "My Profile",
        callback_data="my_profile"
    )
    random_profiles_button = InlineKeyboardButton(
        "View profiles",
        callback_data="random_profiles"
    )
    markup.add(start_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(random_profiles_button)
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


async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "👍🏻",
        callback_data=f"liked_profile_{owner_tg_id}"
    )
    dislike_button = InlineKeyboardButton(
        "👎🏻",
        callback_data="random_profiles"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup
async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Update",
        callback_data=f"update_profile"
    )
    dislike_button = InlineKeyboardButton(
        "Delete",
        callback_data="delete_profiles"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup

