# **Ads parser**

Это проект, написанный на языке:

- Python 3.12

С использованием библиотек/фреймворков:
- Django 5.0.7
- Django REST framework 3.15.2
- drf-spectacular 0.27.2
- PostgreSQL


Backend-составляющая с Django admin интерфейсом и API для просмотра объявлений, 
а также регистрации и авторизацией пользователей.

## **Установка**
### Для установки проекта Ads parser, следуйте инструкциям ниже:

**<p>1. Сделайте Fork этого репозитория. Репозиторий появится в ваших личных репозиториях на GitHub.</p>**

**1.1 Сделайте `git clone` форкнутого репозитория, чтобы получить репозиторий локально:**

**<p>2. Перейдите в папку с проектом.</p>**

**<p>3. Активируйте виртуальное окружение:</p>**

`poetry shell`

**<p>4. Установите зависимости проекта:</p>**

`poetry install`

**<p>5. Создайте файл .env в корневой папке проекта (ad_parser/) и заполните данные для настройки проекта из файла .env.sample:</p>**

```ini
# Django project environment
DJANGO_SECRET_KEY=django_secret_key

# PostgreSQL environment
POSTGRES_DB=db_name
POSTGRES_USER=psql_username
POSTGRES_PASSWORD=psql_password
POSTGRES_HOST=host
POSTGRES_PORT=port

# Superuser environment
SU_EMAIL=your_email@gmail.com
SU_PASSWORD=your_password
```

**<p>6. Примените миграции:</p>**

`python manage.py migrate`

**<p>7. Воспользуйтесь командой для установки русского языка:</p>**

`django-admin compilemessages`

**<p>8. ЗАПУСК BACKEND-ЧАСТИ: Запустите сервер:</p>**

`python manage.py runserver` или настройте запуск Django сервера в настройках.


Таким образом можно работать с backend-частью локально для отладки.

После запуска сервера. Вы сможете перейти на сайт с документацией http://127.0.0.1:8000/api/docs/ 
(если сервер запущен локально), и начать пользоваться всеми API методами проекта. 

Также вы можете схему данных .yaml файлом по адресу http://127.0.0.1:8000/api/schema/ (если сервер запущен локально).

### Либо с помощью Docker
**<p>1. Измените файл .env в корневой папке проекта (ad_parser/), заменив значение в стрчке "POSTGRES_HOST" на Ваше название 
контейнера с базой данных":</p>**
```ini
/.env/

# Django project environment
DJANGO_SECRET_KEY=django_secret_key

# PostgreSQL environment
POSTGRES_DB=db_name
POSTGRES_USER=psql_username
POSTGRES_PASSWORD=psql_password
POSTGRES_HOST=container_name
POSTGRES_PORT=port

# Superuser environment
SU_EMAIL=your_email@gmail.com
SU_PASSWORD=your_password
```

**<p>2. ЗАПУСК BACKEND-ЧАСТИ:: Воспользуйтесь командами:</p>**

`docker compose build` для создания оптимального билда проекта.

`docker compose up` для запуска docker compose контейнера.




## **Использование**
#### На проекте реализована регистрация новых пользователей через django админ-панель или API.
Также есть команда для создания суперпользователя `python manage.py csu` с данными из .env файла

#### Для тестирования вы можете заполнить базу данных данными из фикстур при помощи команды `python manage.py load_ad`
Либо создать свои через django админ-панель.

Просматривать объявления API могут только авторизированные пользователи


Автор
VictorVolkov7 - vektorn1212@gmail.com