import asyncio
import os

import django


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


async def scheduler():
    aioschedule.every().day.at('10:00').do(notify)
    aioschedule.every().day.at('15:00').do(notify)
    aioschedule.every().day.at('18:00').do(notify)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        'admin_panel.admin_panel.settings'
    )
    os.environ.update({"DJANGO_ALLOW_ASYNC_UNSAFE": "true"})
    django.setup()


if __name__ == '__main__':
    setup_django()
    import middlewares, filters, handlers
    from utils import on_startup_notify
    from utils.set_bot_commands import set_default_commands
    from utils.mailing import notify
    import aioschedule
    from aiogram import executor

    from loader import dp

    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())

    executor.start_polling(dp, on_startup=on_startup)
