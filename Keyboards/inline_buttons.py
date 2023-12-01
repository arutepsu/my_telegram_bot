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
    reference_button = InlineKeyboardButton(
        "Reference Link",
        callback_data="reference_link"
    )
    referral_list_button = InlineKeyboardButton(
        "Referral list",
        callback_data="reference_list"
    )
    balance_button = InlineKeyboardButton(
        "Balance",
        callback_data="balance_call"
    )
    anime_news_button = InlineKeyboardButton(
        "View anime news",
        callback_data="anime_news"
    )
    markup.add(start_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(random_profiles_button)
    markup.add(reference_button)
    markup.add(referral_list_button)
    markup.add(balance_button)
    markup.add(anime_news_button)
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


async def admin_keyboard():
    markup = InlineKeyboardMarkup()
    print_all_users_data = InlineKeyboardButton(
        "Print all users data",
        callback_data="all_users"
    )
    print_most_possibly_ban_users_button = InlineKeyboardButton(
        "Print most possible ban user data",
        callback_data="ban_data"
    )
    markup.add(print_all_users_data)
    markup.add(print_most_possibly_ban_users_button)
    return markup


async def private_message_keyboard(link):
    markup = InlineKeyboardMarkup()
    private_message_button = InlineKeyboardButton(
        "Send private message",
        url=link
    )
    markup.add(private_message_button)
    return markup


async def ban_keyboard(link, user_id):
    markup = InlineKeyboardMarkup()

    private_message_button = InlineKeyboardButton(
        "Send private message",
        url=link
    )
    warning_message_button = InlineKeyboardButton(
        "Warning Message",
        callback_data=f"warning_message_{user_id}"
    )
    markup.add(private_message_button)
    markup.add(warning_message_button)
    return markup


async def repeat_survey():
    markup = InlineKeyboardMarkup()

    repeat_button = InlineKeyboardButton(
        "Repeat the Survey",
        callback_data="repeat_survey"
    )
    markup.add(repeat_button)
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


async def save_news_keyboard():
    markup = InlineKeyboardMarkup()
    save_button = InlineKeyboardButton(
        "Save this article",
        callback_data="save_article"
    )
    markup.add(save_button)
    return markup
