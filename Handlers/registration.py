import sqlite3

import aiogram
from aiogram import types, Dispatcher
from config import bot, DESTINATION
from const import USER_DATA_TEXT
from Database.sql_commands import Database
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    nickname = State()
    age = State()
    gender = State()
    location = State()
    bio = State()
    photo = State()


async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Write your nickname!"
    )
    await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="How old are you? \n"
             "(use ONLY numeric text)"
    )
    await RegistrationStates.next()

async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="You provided not numeric text!!!\n"
                 "Try again"
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="What is ur genda?"
    )
    await RegistrationStates.next()

async def load_gender(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Where dou you live?"
    )
    await RegistrationStates.next()

async def load_location(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['location'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="What do you do in free time?"
    )
    await RegistrationStates.next()




async def load_bio(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me your photo fpr your profile pic"
    )
    await RegistrationStates.next()





async def load_photo(message: types.Message,
                     state: FSMContext):
    db = Database()
    path = await message.photo[-1].download(
        destination_dir=DESTINATION
    )
    print(path.name)

    async with state.proxy() as data:
        with open(path.name, 'rb') as photo:
            try:
                await bot.send_photo(
                    chat_id=message.from_user.id,
                    photo=photo,
                    caption=USER_DATA_TEXT.format(
                        nickname=data['nickname'],
                        age=data['age'],
                        gender=data['gender'],
                        location=data['location'],
                        bio=data['bio'],
                    )
                )
            except aiogram.utils.exceptions.BadRequest:
                await bot.send_photo(
                    chat_id=message.from_user.id,
                    photo=photo,
                    caption=USER_DATA_TEXT.format(
                        nickname=data['nickname'],
                        age=data['age'],
                        gender=data['gender'],
                        location=data['location'],
                        bio=data['Down below'],
                    )
                )
                await bot.send_message(
                    chat_id=message.from_user.id,
                    text=data['bio']
                )
            db.insert_sql_user_data_registration(
                telegram_id=message.from_user.id,
                nickname=data['nickname'],
                age=data['age'],
                gender=data['gender'],
                location=data['location'],
                bio=data['bio'],
                photo=path.name
            )
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Registered successfully!"
        )
        await state.finish()


def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "registration"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.gender,
        content_types=['text']
    )
    dp.register_message_handler(
        load_location,
        state=RegistrationStates.location,
        content_types=['text']
    )
    dp.register_message_handler(
        load_bio,
        state=RegistrationStates.bio,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )
