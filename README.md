### Album Project 2023
### Description

### Quick start

Cкопировать файл 
cp example.env .env

Выполнить команды:  
python3 -m venv venv  
source ./venv/bin/activate  
pip install -r requirements.txt  
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver  

### Заполнение баз данных:   
python manage.py loaddata album/fixtures/dump.json 

### Панель администратора:  
http://127.0.0.1:8000/admin/  
  
### Авторизация в браузере:  
http://127.0.0.1:8000/api/v1/drf-authlogin/  

### Документация swagger:  
http://127.0.0.1:8000/swagger/
  
### Postman:  
Создание нового пользователя: POST http://127.0.0.1:8000/api/v1/auth/users/  
Получение токена: POST http://127.0.0.1:8000/auth/token/login  
Разлогиниться: POST http://127.0.0.1:8000/auth/token/logout  

### Командная строка Linux:  
Создание нового пользователя: curl -d "username=Lisa3&password=Lisa3765?:%" -X POST http://localhost:8000/api/v1/auth/users/  
Получение токена: curl -d "username=Lisa3&password=Lisa3765?:%" -X POST http://localhost:8000/auth/token/login/  

### Тесты:


|Name                                 |Stmts|Miss| Cover
|-------------------------------------|-----|----|-----
|album/__init__.py                    |  0  |  0 | 100%
|album/admin.py                       | 31  |  7 |  77%
|album/apps.py                        |  4  |  0 | 100%
|album/filters.py                     | 16  |  0 | 100%
|album/migrations/0001_initial.py     |  8  |  0 | 100%
|album/migrations/__init__.py         |  0  |  0 | 100%
|album/models.py                      | 45  |  6 |  87%
|album/serializer.py                  | 30  |  6 |  80%
|album/tests.py                       | 55  |  0 | 100%
|album/validators.py                  |  9  |  7 |  22%
|album/views.py                       | 28  |  1 |  96%
|app/__init__.py                      |  0  |  0 | 100%
|app/settings.py                      | 26  |  0 | 100%
|app/urls.py                          | 17  |  1 |  94%
|manage.py                            | 12  |  2 |  83%
| TOTAL                               | 281 | 30 |  89%
