from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram import Router, html

from app.keyboards.inline import start_keyboard
from app.keyboards.callbacks.callbacks import MainCallback
from app.texts.user.texts import *

info_router = Router()

@info_router.callback_query(MainCallback.filter(F.action == "info"))
async def command_start_handler(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer(f"{INFO}")

