# API

[master](https://github.com/MoreliaTalk/morelia_server/tree/master) - стабильная ветка.

[dev](https://github.com/MoreliaTalk/morelia_server/tree/dev) - ветка для добавления нового функционала.

## В разработке применяется ##

* [Python 3.9](https://www.python.org/) - язык программирования

* [FastAPI](https://fastapi.tiangolo.com) - основной фреймворк

* [psutil](https://psutil.readthedocs.io/en/latest/g) - python system and process utilities

## Описание репозитория ##

* /mod
  * api.py - модуль отвечает за описание API, а так же валидацию данных.
  * db.py - модуль отвечает за работу БД
  * group.py - модуль отвечает за работу с группами
  * messages.py - модуль отвечает за работу с сообщениями
  * profile.py - модуль отвечает за работу с профилями и аунтефикацией
  * error.py - модуль отвечает за хранение кодов ошибок.
  * logging.py - модуль настройки логирования.
* /templates - шаблоны для вывода статистики сервера в браузере.
  * base.html - базовый шаблон с основными элементами меню, он имплементируется в каждый рабочий шаблон.
  * index.html - рабочий шаблон главной страницы.
  * status.thml - рабочий шаблон страницы со статусом работы сервера.
* app.py - основной код сервера
