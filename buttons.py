from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


jokes_bts = [
    [
        InlineKeyboardButton(text="Хочу анекдот!", callback_data='joke'),
    ],
]

jokes_bts_markup = InlineKeyboardMarkup(inline_keyboard=jokes_bts)


more_jokes_bts = [
    [
        InlineKeyboardButton(text="Еще анекдот!", callback_data='joke'),
    ],
]

more_jokes_bts_markup = InlineKeyboardMarkup(inline_keyboard=more_jokes_bts)