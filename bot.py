import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from joke import get_joke
from buttons import jokes_bts_markup, more_jokes_bts_markup

TOKEN = "6214938447:AAGqIuN6P0UDQFF4G3OGH3BN2EDt6fv4Bm0"
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

db = Dispatcher()

@db.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")


@db.message(Command('commands'))
async def commands(message: Message):
    await message.answer("Нажмите на кнопку", reply_markup=jokes_bts_markup)


@db.message()
async def get_anekdot_handler(message: Message):
    if message.text == 'Хочу анекдот':
        joke = get_joke()
        await message.answer(joke)


@db.callback_query(lambda c: c.data == 'joke')
async def send_message(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id

    joke = get_joke()
    await bot.send_message(chat_id, joke, reply_markup=more_jokes_bts_markup)



async def main() -> None:
    await db.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())