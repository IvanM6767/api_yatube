# CRUD для Yatube

[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-464646?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Pytest](https://img.shields.io/badge/Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Postman](https://img.shields.io/badge/Postman-464646?style=flat-square&logo=postman)](https://www.postman.com/)

Яндекс Практикум. Спринт 8. Итоговый проект. CRUD для Yatube.

## Описание

CRUD для проекта социальной сети Yatube.

## Функционал

- Реализован REST API для сервиса публикации постов, Yatube;
- Аутентификация по JWT-токену;
- Работает со всеми модулями Yatube: постами, комментариями, группами и подписчиками.
- Поддерживает методы GET, POST, PUT, PATCH, DELETE;
- Предоставляет данные в формате JSON.

## Установка

1. Клонировать репозиторий:

   ```python
   git clone https://github.com/IvanM6767/api_yatube.git
   ```

2. Перейти в папку с проектом:

   ```python
   cd api_yatube/
   ```

3. Установить виртуальное окружение для проекта:

   ```python
   python -m venv venv
   ```

4. Активировать виртуальное окружение для проекта:

   ```python
   # для OS Lunix и MacOS
   source venv/bin/activate
   # для OS Windows
   source venv/Scripts/activate
   ```

5. Установить зависимости:

   ```python
   python3 -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Выполнить миграции на уровне проекта:

   ```python
   cd yatube
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

## Аутентификация

1. Выполнить POST-запрос к ручке `http://localhost:8000/api/v1/token/` передав поля `username` и `password`.

2. Получить от API JWT-токен в формате:

   ```json
   {
     "refresh": "xxx",
     "access": "xxx"
   }
   ```

3. В поле `access` вернётся токен. Данные в поле `refresh` будут необходимы для обновления токена.

4. При отправке запроcов передать токен в заголовке `Authorization: Bearer <токен>`.

## Примеры запросов

Результат POST-запроса с токеном пользователя на добавление нового поста:

1. Пример запроса:

   ```python
   {
       "text": "Текст",
       "group": 1
   }
   ```

2. Пример ответа:

   ```python
   {
       "id": 1,
       "text": "Текст",
       "author": "Имя",
       "image": null,
       "group": 1,
       "pub_date": "2022-11-11T08:47:10.084572Z"
   }
   ```
