from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def action(telegram_id, username, phone):
    choose = InlineKeyboardMarkup(row_width=3,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Подтвердить',
                                                               callback_data=f'accept|{telegram_id}|{username}|{phone}'),
                                          InlineKeyboardButton(text='Отказать', callback_data=f'deny|{telegram_id}')
                                      ]
                                  ])

    return choose
