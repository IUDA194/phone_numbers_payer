FROM python

# Устанавливаем переменную среды для запуска в режиме неинтерактивного режима
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /bot

# Копируем файлы зависимостей в контейнер
COPY requirements.txt /bot/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект в контейнер
COPY . /bot/

# Запускаем команду для запуска сервера Django
CMD python bot.py