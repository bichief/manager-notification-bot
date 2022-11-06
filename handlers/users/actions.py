from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp
from utils.db_api.db_commands import create_client


@dp.callback_query_handler(Text(startswith='accept'))
async def accept_action(call: types.CallbackQuery):
    await call.answer('Заявка успешно одобрена!')
    await call.message.delete()

    data = call.data.split('|')

    await create_client(telegram_id=data[1], username=data[2], phone=data[3])
    await dp.bot.send_message(
        chat_id=data[1],
        text='Отличные новости!\n'
             'Ваша заявка была одобрена, теперь вы подписаны на рассылку.'
    )


@dp.callback_query_handler(Text(startswith='deny'))
async def deny_action(call: types.CallbackQuery):
    await call.answer('Заявка успешно отклонена!')

    data = call.data.split('|')

    await dp.bot.send_message(
        chat_id=data[1],
        text='К сожалению, ваша заявка была отклонена.'
    )
