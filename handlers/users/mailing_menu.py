from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data import config
from loader import dp
from states.get_information import Mailing
from utils.db_api.db_commands import select_managers


@dp.message_handler(Command('a'), user_id=config.ADMINS)
async def pre_mailing(message: types.Message):
    await message.answer('Отправь мне Text/Voice message to mailing')
    await Mailing.message.set()


@dp.message_handler(state=Mailing.message)
async def go_mailing(message: types.Message, state: FSMContext):
    managers = await select_managers()
    if message.text:
        for manager in managers:
            await dp.bot.send_message(
                chat_id=manager.telegram_id,
                text=message.text,
            )
    else:
        await message.answer('Я такое не понимаю')

    await state.reset_state()
