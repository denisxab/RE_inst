# Используем лековесный образ `Alpine Linux`
FROM python:3.9-alpine

# Робочая директория
WORKDIR /usr/src/re_inst

ENV                             \
    # Не создавать папку `.pyc` для кеширование байт кода.
    PYTHONDONTWRITEBYTECODE=1   \
    # Не кешировать вывод из консоли.
    PYTHONUNBUFFERED=1

COPY                    \
    # Явно скопировать файл с зависемостями.
    requirements.txt .  \
    # Скопировать все файлы.
    .                   \
    ./


RUN                           \
    # Обновить `pip`
    pip install --upgrade pip;\
    # Установить зависемости из файла
    pip install -r requirements.txt;

# Открыть указанный порт в контейнере (подсказка).
EXPOSE 8080

# Запустить сервер при запуске контейнера.
CMD python re_view/manage.py runserver 0.0.0.0:8080
