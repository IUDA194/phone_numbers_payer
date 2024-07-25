from aiogram.filters.callback_data import CallbackData

class MainCallback(CallbackData, prefix="send_excel"):
    action: str