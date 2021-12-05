

Внешний вид.
![Внешний вид](https://i.imgur.com/dvmzOfy.png)

---
Установка:

```bash
git clone https://github.com/denisxab/RE_inst.git;
cd RE_inst;
python -m venv venv_dj && . venv_dj/bin/activate;
pip install -r req.txt;
cd re_view;
python manage.py migrate;
```

Запуск:
```bash
python manage.py runserver
```
---

Проект написан на `Django`. Его цель - интерактивное 
выполнение регулярных выражений.

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