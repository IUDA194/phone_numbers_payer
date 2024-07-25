from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

from app.keyboards.callbacks import callbacks

def start_keyboard(user_id : str) -> InlineKeyboardMarkup:
    start_keyboard = InlineKeyboardBuilder()
    
    start_keyboard.row(
        InlineKeyboardButton(text="💸 Відправити таблицю для виплат", callback_data=callbacks.MainCallback(action="send").pack())
    )
    start_keyboard.row(
        InlineKeyboardButton(text="📍 Інфо", callback_data=callbacks.MainCallback(action="info").pack())
    )
    
    return start_keyboard.as_markup()