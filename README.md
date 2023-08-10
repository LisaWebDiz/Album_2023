### Запуск

Выполнить команду: cd TestTask/album  
  
Создать файл .env в TestTask/TestTask с данными:  
SECRET_KEY=''  
DEBUG=True  
DB_ENGINE=''  
DB_NAME=''  
DB_USER=''  
DB_PASSWORD=''  
DB_HOST=''  
DB_PORT=''  

Выполнить команды:  
python 3 -m venv venv  
. ./venv/bin/activate  
pip install -r requirements.txt  
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver  

### Заполнение баз данных:   
python manage.py loaddata ./*/fixtures/*.json  

### Панель администратора:  
http://127.0.0.1:8000/admin/  
Логин: Lisa  
Пароль: Lisa  
  
### Авторизация в браузере:  
http://127.0.0.1:8000/api/v1/drf-authlogin/  

### Документация swagger:  
http://127.0.0.1:8000/swagger/
  
### Postman:  
Создание нового пользователя: GET http://127.0.0.1:8000/api/v1/auth/users/  
Получение токена: POST http://127.0.0.1:8000/auth/token/login  
Разлогиниться: POST http://127.0.0.1:8000/auth/token/logout  

### Командная строка Linux:  
Создание нового пользователя: curl -d "username=Lisa3&password=Lisa3765?:%" -X POST http://localhost:8000/api/v1/auth/users/  
Получение токена: curl -d "username=Lisa3&password=Lisa3765?:%" -X POST http://localhost:8000/auth/token/login/  

### Тесты:

| Name                                                                               | Stmts | Miss | Cover 
|------------------------------------------------------------------------------------|:------|:-----|:------
| TestTask/__init__.py                                                               |    0  |    0 |  100%
| TestTask/settings.py                                                               |    26 |    0 |  100%
| TestTask/urls.py                                                                   |    13 |    1 |   92%
| album/__init__.py                                                                  |     0 |    0 |  100%
| album/admin.py                                                                     |    29 |    7 |   76%
| album/apps.py                                                                      |     4 |    0 |  100%
| album/migrations/0001_initial.py                                                   |     6 |    0 |  100%
| album/migrations/0002_user_alter_album_options_remove_album_author_and_more.py     |     5 |    0 |  100%
| album/migrations/0003_remove_photo_category_photo_category.py                      |     4 |    0 |  100%
| album/migrations/0004_album_exist_photo_exist_alter_photo_category.py              |     4 |    0 |  100%
| album/migrations/0005_alter_album_options_remove_album_exist_and_more.py           |     6 |    0 |  100%
| album/migrations/0006_alter_photo_thumbnail.py                                     |     5 |    0 |  100%
| album/migrations/0007_remove_photo_thumbnail.py                                    |     4 |    0 |  100%
| album/migrations/0008_alter_photo_album.py                                         |     5 |    0 |  100%
| album/migrations/0009_remove_photo_album_remove_photo_category_and_more.py         |     4 |    0 |  100%
| album/migrations/0010_album_photo.py                                               |     6 |    0 |  100%
| album/migrations/0011_alter_user_options_remove_user_name_and_more.py              |     4 |    0 |  100%
| album/migrations/0012_alter_album_user_delete_user.py                              |     6 |    0 |  100%
| album/migrations/0013_alter_photo_options_remove_album_photos_quantity_and_more.py |     6 |    0 |  100%
| album/migrations/__init__.py                                                       |     0 |    0 |  100%
| album/models.py                                                                    |    50 |    7 |   86%
| album/permissions.py                                                               |    11 |    6 |   45%
| album/serializer.py                                                                |    30 |    6 |   80%
| album/tests.py                                                                     |    55 |    0 |  100%
| album/tests_api/__init__.py                                                        |     0 |    0 |  100%
| album/tests_api/test_api.py                                                        |     0 |    0 |  100%
| album/urls.py                                                                      |     3 |    0 |  100%
| album/validators.py                                                                |     9 |    7 |   22%
| album/views.py                                                                     |    44 |    1 |   98%
| manage.py                                                                          |    12 |    2 |   83%
| 
| TOTAL                                                                              |   351 |   37 |   89%

