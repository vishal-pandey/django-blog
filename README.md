# django-blog

Admin Panel Link  
https://django-blog.vishalpandey.co.in/admin/  


### Instructions for running it locally
```
git clone https://github.com/vishal-pandey/django-blog/
cd django-blog
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
Edit app/settings.py   
and change mysql Database Name, Username, Password and host according your local database settings  
```
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecomm',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
    },
    'product': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

```
```
python manage.py migrate
python manage.py createsuperuser
```
Provide email and password for the superuser admin panel
```
python manage.py runserver
open https://127.0.0.1:8000
```
