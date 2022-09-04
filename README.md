# RG : IOT

# How to run the app local

1. Clone the project.
2. Create smartconnect schema and load the latest dump from dev.
3. Navigate to project and update the .env file.
4. pip install virtualenv
5. virtualenv env
6. env\scripts\activate or for ubuntu (source env/bin/activate)
7. pip install -r requirements\dev.txt
8. python manage.py migrate
9. python manage.py createsuperuser --email email@birchford.com --username admin (optional)
10. python manage.py runserver

find ../smart-connect-processor/ -name "*.pyc" -type f -delete

python manage.py dumpdata rest processing --exclude rest.UserOrganization --exclude contenttypes > fixtures/dump.json

docker build --no-cache -t sc-new-gen .

find ../smart-connect-processor/ -name "*.pyc" -type f -delete

# Command for ubuntu subsystem with postgres in docker
docker run --name sc-new-gen --env-file env.list --link  birchfordtimescaledb:localhost \
-v /var/log/smartconnect/:/var/log/smartconnect/ \
-v /home/nileshbhosale/workspace/smart-connect-templates/:/home/project/smart-connect-templates/ \
-v /home/nileshbhosale/workspace/smart-connect-processor/certs/:/home/project/certs/ \
-t sc-new-gen

# Command for ubuntu subsystem with local postgres.
sudo docker run --restart always  --name sc-new-gen --env-file env.list \
--network=host \
-v /var/log/smartconnect/:/var/log/smartconnect/ \
-v /home/project/smart-connect-templates/:/home/project/smart-connect-templates/ \
-v /home/project/certs/:/home/project/certs/ \
-t 0dfa4535395e

sudo docker-compose up 

# Command for windows with local postgres:- 
docker run --name sc-new-gen-uat --env-file env.list.txt -p 8080:8080  -v C:\smart-connect\logs\:/var/log/smartconnect/ -v C:\smart-connect\templates\:/home/project/smart-connect-templates/ -v C:\smart-connect\certs\:/home/project/certs/ -t a2eede7cf803

# Command for windows with Docker postgres:- 
docker run --name sc-new-gen-uat --env-file env.list.txt --link  birchfordtimescaledb:localhost -p 8080:8080  -v C:\smart-connect\logs\:/var/log/smartconnect/ -v C:\smart-connect\templates\:/home/project/smart-connect-templates/ -v C:\smart-connect\certs\:/home/project/certs/ -t 87d79bb2e86c






# Prod SC
sudo docker run --name sc-new-gen --env-file env.list \
--network=host \
-v /var/log/smartconnect/:/var/log/smartconnect/ \
-v /home/hhadmin/project/smart-connect-templates/:/home/hhadmin/project/smart-connect-templates/ \
-v /home/hhadmin/project/certs/:/home/hhadmin/project/certs/ \
-t e9aff3220fdf




pg_restore sc-uat-17-05-2021 -U postgres -h 172.29.132.8 -d kuwait-uat < sc-uat-17-05-2021
pg_dump  -U postgres -h 172.29.132.8 -d kuwait-uat > sc-uat-18-05-2021
