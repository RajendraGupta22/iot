# RG : IOT 
### Author : Rajendra Gupta
### email : raj.shadow.gupta@gmail.com

#
# How to run the app local

1. Clone the project.
2. install and setup virtualenv if not present in repository.
3. in general venv virtualenv is pushed too.
4. installl requirement.txt if new virtual env
5. pip install -r requirements.txt
6. python manage.py runserver

# Admin Login Creds :
1. username = ***
2. password = ***

# Urls to access :
1. /admin/ : to access django admin
2. "" : openapi doc for the rest api's
3. api-token-auth/ : jwt token generation
4. api-token-refresh/ : jwt token refresh
5. api-token-verify/ : jwt token verify
6. rest-api/ : rest-api's for iot

# Authentication Mechanism used:
## authentication order is as follows -
1. JWT
2. Session
3. Basic

# API info :
- Api's can be accessed and tested from rest framework UI in browser with the Url mentioned above
- The api can be tested from postman or any of the api calling tool/method/approach.

