from aiogram import executor
from config import dp
from Handlers import (
    start,
    call_back,
    chat_actions,
    registration,
    profiles,
    reference,
    balance,
    admin,
    survey,
    survey_list,
)
from Database import sql_commands


async def on_startup(_):
    db = sql_commands.Database()
    db.create_sql_tables()


start.register_start_handlers(dp=dp)
call_back.register_callback_handlers(dp=dp)
admin.register_admin_handlers(dp=dp)
chat_actions.register_chat_actions_handlers(dp=dp)
registration.register_registration_handlers(dp=dp)
profiles.register_profile_handlers(dp=dp)
reference.register_reference_handlers(dp=dp)
balance.register_balance_handlers(dp=dp)
survey.register_survey_handlers(dp=dp)
survey_list.register_survey_list_handlers(dp=dp)
if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )
