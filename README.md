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
