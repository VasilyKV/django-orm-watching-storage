# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников банка.

Доступные страницы:  
1. Список активных карт доступа;
2. Список пользователей в хранилище;
3. Список посещений хранилища выбранным пользователем. 

В случае, если длительность посещения будет превышать 60 минут, в графе "Был ли визит подозрителен" отобразится статус True

### Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

`pip install -r requirements.txt`

Для запуска сайта с консоли используйте команду: 
```cmd
python manage.py runserver 0.0.0.0:8000
```


### Переменные окружения
Необходимо создать файл .env, в котором должны быть указаны значения следующих переменных:  
ENGINE = {}  
HOST = {}  
PORT = {}  
NAME = {}  
USER = {}  
PASSWORD = {}  
SECRET_KEY = {}  
DEBUG = {True/False}


### Цели проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
