libraries ```pip install Django==3.0.2 django-rest-framework django-oauth-toolkit django-crum```

virtual environment: ```python -m venv ./venv```   ```source ./venv/bin/activate```

start server: ```python src/manage.py runserver 172.31.47.107:9999```

running job scheduling: ```python src/manage.py process_tasks```

after change to tasks.py file: ```python src/manage.py migrate```

view site: ```http://54.173.178.23:9999/admin/```

username: admin
password: admin

when changing models:
```python manage.py makemigrations```
```python manage.py migrate```
