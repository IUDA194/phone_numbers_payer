import asyncio
import logging
import sys

from dotenv import load_dotenv, find_dotenv
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from app import (
    hendlers,
    keyboards
)

from app.hendlers import (
    start_router, send_exel_router, info_router
)

load_dotenv(find_dotenv())

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    dp.include_router(start_router)
    dp.include_router(send_exel_router)
    dp.include_router(info_router)
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())