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



**Introduction

This write up provides a brief explanation of the auction app i have built. It was created by
myself without a partner. First we will discuss project structure and how I installed the
framework. I will describe the REST endpoints with an example of how they are used. Then I will
describe the database model and application implementation.

**Directory Structure

The src/auction directory provides the main app functionality of storing auctions and allowing
users to bid on them. Most of the app functionality is provided through four files: views.py,
models.py, tests,py and serializers.py. We have a src/users directory which manages
authentication and user storage. The functionality is provided by views.py. This is not modified
from the sample provided. We also have an src/api directory which stores the application config.
The top level urls of the app are specified in urls.py here.
There is a test folder containing unit tests and a venv folder which contains the python virtual
environment. A virtual environment is used so we have a local copy of python and its
dependencies. We use pip for dependency installation. The test folder contains helpers.py
which provide python methods that encapsulate the endpoints.

More details can be found in the GitHub repository
https://github.com/neilshah2000/cloud-auction

**Framework

The application framework is Django and uses OAuth2TokenMiddleware and
CurrentRequestUserMiddleware to authenticate and store users. It also used the
django-background-tasks library to schedule jobs for ending auctions.

**Installation

The application is hosted on an AWS instance of Ubuntu Server 18.04 LTS. It is t2.medium
build with 2 cores and 4GB of RAM.
The API root can be accessed here http://54.173.178.23:9999/auction/

**Authentication

Authentication is provided by the OAuth2TokenMiddleware, a Django plugin. The responsibility
for authentication is handed over to the users service. We create an application configuration
with a secret token and register it with the service. When our auction app wants to interact with
the authentication service it presents the secret token for the app plus whatever credentials the
user has supplied, and returns an access token the user can reuse for the rest of their session.

**REST API

The top level server domain url is 'http://54.173.178.23:9999/'. Endpoints below are relative to
that.
- getToken = [POST] authentication/token/
- addBid = [POST] auction/bid/
- getBids = [POST] auction/auctionItem/56/bids/
- getItem = [GET] auction/auctionItem/23
- getAllItems = [GET] auction/auctionItem/
- getAllAvailableItems = [GET] auction/auctionItem/available/
- getSoldItems = [GET] auction/auctionItem/sold/
- addAuctionItem = [POST] auction/auctionItem/

**Posting a Bid

Login
POST http://54.173.178.23:9999/authentication/token/ 
  {'username': 'mary', 'password': 'mary'}
POST http://54.173.178.23:9999/authentication/token/ 
  {'username': 'olga', 'password': 'olga'}

Create Auction
POST http://54.173.178.23:9999/auction/auctionItem/
Authorization: Bearer m28FwpnCkzGmxTv5UiusqsAcga4QRo
  {
    "title": "new item",
    "description": "item description",
    "price": 1.0,
    "endDate": "2020-04-19T12:03:34.910369Z"
    "condition": "Used"
  }

Bid
POST http://54.173.178.23:9999/auction/bid/
Authorization: Bearer m28FwpnCkzGmxTv5UiusqsAcga4QRo
  {
    "amount": 70.0,
    "item": 20
  }

**Database Schema

***Auction Item

title: String
description: String
condition: Enum
models: Float
endDate: DateTime
ended: Boolean
winner: FK(User)
created_by: FK(User)
created_at: DateTime

***Bid

amount: Float
time: DateTime
item: FK(Auction)
created_by: FK(User)

**Implementation

I use the ModelViewSet to create the views I pass into the router. This gives me prebuilt CRUD
methods which I extend to create more functionality for my endpoints. When an auction is
created, I configure a task for the Django background task library with a timestamp. This then
ends the auction and calculates the winning bid which it adds to the auction model row.
Future work
Auction has a (start)price field which is not really used. When the auction ends it can be used to
store the winning price.
The auction create endpoint requires a start time. This is UTC time format and hard for the user
to enter. There is also a timezone difference between the server and user which affects start
time. This functionality needs to be made more useful.

**References

https://docs.djangoproject.com/en/dev/ref/models/fields/#field-choices-enum-types
https://www.django-rest-framework.org/api-guide/viewsets/
https://docs.djangoproject.com/en/3.0/ref/applications/
https://django-background-tasks.readthedocs.io/en/latest/
https://www.django-rest-framework.org/api-guide/routers/
https://www.django-rest-framework.org/api-guide/serializers/
