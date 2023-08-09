Выполнить команду: cd TestTask/album  
Создать файл .env в TestTask/TestTask с данными:  
  
SECRET_KEY='django-insecure-n%i%zp+2(c*v2!*2*1v%sv&g#62ib^jkg2($&6cj2h34xo7rxu'  
DEBUG=True  

Выполнить команды:  
python 3 -m venv venv  
. ./venv/bin/activate  
pip install -r requirements.txt  
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver  
  
Панель администратора:  
http://127.0.0.1:8000/admin/  
Логин: Lisa  
Пароль: Lisa  
  
Авторизоваться в браузере:  
http://127.0.0.1:8000/api/v1/drf-authlogin/  
  
Postman:  
Создать нового пользователя: GET http://127.0.0.1:8000/api/v1/auth/users/  
Получить токен: POST http://127.0.0.1:8000/auth/token/login  
Разлогиниться: POST http://127.0.0.1:8000/auth/token/logout  
