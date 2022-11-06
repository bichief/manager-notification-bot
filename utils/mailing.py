from loader import dp
from utils.db_api.db_commands import select_managers


async def notify():
    managers = await select_managers()

    for manager in managers:
        await dp.bot.send_message(
            chat_id=manager.telegram_id,
            text='Пришло время проверить заявки.',
        )
