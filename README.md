Выполнить команду: cd TestTask/album  
  
Создать файл .env в TestTask/TestTask с данными:  
SECRET_KEY=''  
DEBUG=True  

Выполнить команды:  
python 3 -m venv venv  
. ./venv/bin/activate  
pip install -r requirements.txt  
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver  

Заполнение баз данных: python manage.py loaddata ./*/fixtures/*.json  

Панель администратора:  
http://127.0.0.1:8000/admin/  
Логин: Lisa  
Пароль: Lisa  
  
Авторизация в браузере:  
http://127.0.0.1:8000/api/v1/drf-authlogin/  

Документация swagger:  
http://127.0.0.1:8000/swagger/
  
Postman:  
Создание нового пользователя: GET http://127.0.0.1:8000/api/v1/auth/users/  
Получение токена: POST http://127.0.0.1:8000/auth/token/login  
Разлогиниться: POST http://127.0.0.1:8000/auth/token/logout  

Командная строка Linux:  
Создание нового пользователя: curl -d "username=Lisa3&password=Lisa3765?:%" -X POST http://localhost:8000/api/v1/auth/users/  
Получение токена: curl -d "username=Lisa3&password=Lisa3765?:%" -X POST http://localhost:8000/auth/token/login/
