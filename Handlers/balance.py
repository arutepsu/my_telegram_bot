from aiogram import types, Dispatcher
from config import bot
from Database.sql_commands import Database


async def balance_call(call: types.CallbackQuery):
    db = Database()
    data = db.sql_select_balance_referral(tg_id=call.from_user.id)

    if data:
        balance = data.get("balance")
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Your balance is: {balance}\n"
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="No data found for your balance. Your balance is 0"
        )


def register_balance_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(balance_call,
                                       lambda call: call.data == "balance_call")
