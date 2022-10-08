# API для проекта YamDB

## Описание проекта

Реализация API для проекта YamDB.
Документация лежит по адресу http://127.0.0.1:8000/redoc/


### Список некоторых используемых технологий/пакетов:

* Django==2.2.16
* django-filter==21.1
* djangorestframework==3.12.4
* djangorestframework-simplejwt==5.2.1
* requests==2.26.0
* PyJWT==2.1.0



### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:1karp/api_yamdb.git
```
```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```




## Примеры запросов

```
Категории: GET /api/v1/categories/
Жанры: GET /api/v1/genres/
Произведения:GET  /api/v1/titles/
Отзывы: GET /api/v1/titles/{title_id}/reviews/
Комментарии: GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
