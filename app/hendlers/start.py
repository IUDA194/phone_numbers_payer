from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router
from aiogram import Router, html

from app.keyboards.inline import start_keyboard

start_router = Router()

@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=start_keyboard(message.from_user.id))

