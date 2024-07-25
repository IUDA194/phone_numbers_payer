from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram import F, Router, Bot
from aiogram import Router, html
from aiogram.fsm.context import FSMContext

from dotenv import load_dotenv, find_dotenv
from os import getenv
from os.path import exists

from app.keyboards.inline import start_keyboard
from app.keyboards.callbacks.callbacks import MainCallback
from app.states import Excel_File_State
from app.utils.main import array_to_excel, excel_to_dict_array, top_up_phone

from datetime import datetime
from uuid import uuid1

load_dotenv(find_dotenv())

TOKEN = getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)

send_exel_router = Router()

@send_exel_router.callback_query(MainCallback.filter(F.action == "send"))
async def button_send_excel_handler(callback_query: CallbackQuery, state: FSMContext) -> None:
    await callback_query.message.answer(f"Відправте файл з інформацією для виплат:")
    await state.set_state(Excel_File_State.file)

@send_exel_router.message(Excel_File_State.file)
async def excel_file_hendler(message: Message, state: FSMContext) -> None:
    document = message.document
    if document and (document.file_name.endswith(".xlsx") or document.file_name.endswith(".xls")):
        file_info = await bot.get_file(document.file_id)
        file_path = file_info.file_path
        destination = "tmp/" + document.file_name

        # Download the file
        await bot.download_file(file_path, destination=destination)
        
        await message.answer("Файл оброблюється, зачекайте")
        
        top_ups = excel_to_dict_array(destination)
        
        for top_up in top_ups:
            if top_up['Статус'] == '':
                result = top_up_phone(top_up['Номер'], top_up['Сума'])
                
                print(result)
                
                top_up['Статус'] = result['status']
                top_up['Айді'] = result['id']
                top_up['Дата'] = datetime.now().date().isoformat()
                
            else:
                top_up['Дата'] = datetime.now().date().isoformat()
                top_up['Айді'] = ' - '
        
        try:
            result_path = array_to_excel(top_ups, destination)
            # Проверяем, существует ли файл перед отправкой
            if exists(result_path):
                inp_file = FSInputFile(path=result_path, filename=result_path)
                    
                await message.answer_document(document=inp_file)
            else:
                await message.answer("Файл не був збережений коректно!")
        except Exception as e:
            await message.answer(f"Помилка збереження або відправки файлу: {e}")
        
    else:
        await message.answer("Надішліть excel(.xlsx) файл для опрацювання!")
