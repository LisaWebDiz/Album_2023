# Album Project 2023

### Description
A web application for creating and managing personal photo albums. A registered user can create albums, upload and store images, and view or manage only their own content. A custom manage.py command is included for initial database population with sample data. Media files are organized and served via Django’s static and media file configuration. Strong permissions: each user can only access their own albums and media.

### Quick start
```bash
git clone https://github.com/yourusername/album_2023.git
cd album_2023.git
cp example.env .env

python3 -m venv venv  
source ./venv/bin/activate  
pip install -r requirements.txt  
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver  

python manage.py loaddata album/fixtures/dump.json 
```
Enjoy!

### API Documentation:  
• Swagger UI: http://localhost:8000/swagger/
• Redoc: http://localhost:8000/redoc/
 
### Web authorization:  
http://127.0.0.1:8000/api/v1/drf-authlogin/  
  
### Postman:  
Create a new user: POST http://127.0.0.1:8000/api/v1/auth/users/  
Obtain token: POST http://127.0.0.1:8000/auth/token/login  
Log out: POST http://127.0.0.1:8000/auth/token/logout  

### Linux:  
New user creation: curl -d "username=Lisa3&password=Lisa3765?:%" -X POST http://localhost:8000/api/v1/auth/users/  
Getting token: curl -d "username=Lisa3&password=Lisa3765?:%" -X POST http://localhost:8000/auth/token/login/

### Key Features
    • User registration & authentication: out-of-the-box with Django and Djoser API
    • Security: Users have access only to their own albums and photos — no cross-user visibility
    • Django admin panel for managing data at http://localhost:8000/admin/
    • Fully documented REST API
    • Data storage using PostgreSQL
    • Built-in pgAdmin interface for managing the database at http://localhost:5050
    • Admin panel: http://localhost:8000/admin/
    • Catalogue list view and detail view for albums
    • Add / edit / delete entries — available for registered users
 
### Tests:
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
