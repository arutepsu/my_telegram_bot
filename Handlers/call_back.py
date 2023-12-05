
import sqlite3

from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery

from config import bot, dp
from Database.sql_commands import Database
from Keyboards.inline_buttons import survey_keyboard, repeat_survey, save_news_keyboard
from scraping.anime_news_scraper import AnimeNewsScraper
from scraping.async_anime_news_scraper import AsyncNewsScraper


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


async def scraper_call(call: types.CallbackQuery):
    scraper = AnimeNewsScraper()
    data = scraper.parse_data()
    db = Database()

    for url in data[:5]:
        print("URL from scraper:", scraper.PLUS_URL + url)
        id = db.get_news_id_by_link(scraper.PLUS_URL + url)
        print("ID from database:", id)
        # print("!!!", url)
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"{scraper.PLUS_URL + url} ",
            reply_markup=await save_news_keyboard(article_id=id)
        )


async def save_news_callback_handler(call: CallbackQuery):
    data_parts = call.data.split('_')
    if len(data_parts) >= 2:
        link_id = '_'.join(data_parts[2:])
        db = Database()
        link = db.get_news_link_by_id(link_id)
        print(link)
        if link:
            try:
                db.sql_insert_favorite_news_element(
                    tg_id=call.from_user.id,
                    link=link
                )
                await bot.send_message(
                    chat_id=call.from_user.id,
                    text="Article Saved!"
                )
            except sqlite3.IntegrityError:
                await bot.send_message(
                    chat_id=call.from_user.id,
                    text="Article is already saved!"
                )
        else:
            await bot.send_message(
                chat_id=call.from_user.id,
                text="Failed to retrieve the article link. Please try again later."
            )
    else:
        print("Invalid callback data format")


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
    dp.register_callback_query_handler(scraper_call,
                                       lambda call: call.data == "anime_news")
    dp.register_callback_query_handler(save_news_callback_handler,
                                       lambda call: call.data.startswith('save_article_'))
