import pandas as pd
from app.utils.config import number_row, sum_row

from uuid import uuid1

def excel_to_dict_array(file_path, sheet_name=0):
    """    
    :param file_path: Путь к файлу Excel.
    :param sheet_name: Имя листа или его индекс (по умолчанию первый лист).
    :return: Массив словарей с валидированными данными.
    """
    # Считываем данные из файла Excel
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    except FileNotFoundError: 
        raise FileNotFoundError("File not found")
    # Преобразуем DataFrame в массив словарей
    dict_array = df.to_dict(orient='records')
    
    for top_up in dict_array:
        top_up["Статус"] = ""
        top_up["Дата"] = ""
        top_up["Айді"] = ""
        if str(top_up[number_row]).startswith("38"):
            top_up[number_row] = int(str(top_up[number_row]).replace("38", ""))
        if str(top_up[number_row]).startswith("+38"):
            top_up[number_row] = int(str(top_up[number_row]).replace("+38", ""))
        if len(str(top_up[number_row])) < 9:
            top_up["Статус"] = f"Помилка - Номер - {top_up[number_row]} - Повинен бути довше ніж 8"
        try:
            int(top_up[number_row])
        except ValueError:
            top_up["Статус"] = f"Помилка - Номер - {top_up[number_row]} - Повинен бути числом"
        try:
            top_up[sum_row] = int(top_up[sum_row])
            if top_up[sum_row] <= 0:
                top_up["Статус"] = f"Помилка - Сума - {top_up[sum_row]} - Повинна бути більше нуля"
        except ValueError:
            top_up["Статус"] = f"Помилка - Сума - {top_up[sum_row]} - Повинна бути числом"
    
    return dict_array

def array_to_excel(arr, name: str):
    # Удаляем расширение .xlsx, если оно есть
    if name.endswith(".xlsx"):
        name = name[:-5]

    # Создаем имя файла с расширением .xlsx
    output_path = name + ".xlsx"

    # Сохраняем DataFrame в Excel файл
    pd.DataFrame(arr).to_excel(output_path, index=False)

    return output_path

def top_up_phone(number : int, amount: int):
    id = uuid1().hex
    
    return {"status" : "Помилка інтеграції з сервісом", "id" : id}