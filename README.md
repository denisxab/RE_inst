# Внешний вид.

![Внешний вид](https://i.imgur.com/Zn6hNqn.png)

# Установка:

Используя виртуальное окружение `Python`

```bash
git clone https://github.com/denisxab/RE_inst.git;
cd RE_inst;
python -m venv venv_dj && . venv_dj/bin/activate;
pip install -r requirements.txt;
cd re_view;
```

Запуск:

```bash
python manage.py runserver 127.0.0.1:8080
```

---

Используя `Docker` (Вес образа `99.1 мб`)

```bash
git clone https://github.com/denisxab/RE_inst.git;
cd RE_inst;
docker build -t re_inst .;
```

Запуск:

```bash
docker run -ti --rm  --name re_inst_canteiner -p 8080:8080  re_inst;
```

# О чем проект ?

Проект написан на `Django`. Его цель - интерактивное выполнение регулярных выражений.

---
Поддерживаемые регулярные функции:

- match
- search
- findall
- split
- sub

---

[Моя документация про регулярные выражения](https://github.com/denisxab/open_lessen/blob/main/%D0%A3%D1%80%D0%BE%D0%BA%D0%B8/%D0%91%D0%BB%D0%BE%D0%BA9%20-%20Re%2C%20Unit-Tests.md)

---