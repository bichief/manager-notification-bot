from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.get_number import num
from loader import dp
from utils.db_api.db_commands import select_client


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    manager = await select_client(telegram_id=message.chat.id)
    if len(manager) != 0:
        await message.answer('Вы уже авторизованы!')
    else:
        await message.answer(f"Привет, {message.from_user.full_name}!\n\n"
                             f"Нажми на кнопку ниже, чтобы оставить свой номер.", reply_markup=num)
