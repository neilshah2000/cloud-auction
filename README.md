libraries ```pip install Django==3.0.2 django-rest-framework django-oauth-toolkit```
virtual environment: ```python -m venv ./venv```   ```source ./venv/bin/activate```
start server: ```python src/manage.py runserver 172.31.80.164:9999```

view site: ```http://3.92.177.227:9999/admin/```

username: admin
password: admin

when changing models:
```python manage.py makemigrations```
```python manage.py migrate```