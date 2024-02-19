from django.db import models

# Commands to run for setup
#start_postgres
# pip install --upgrade distro-info
# pip3 install --upgrade pip==23.2.1


# Test model
class Test(models.Model):
    name = models.CharField(max_length=30)

##### Commands to run in terminal for testing:
# cd ormtemplate

# pip install virtualenv
# virtualenv djangoenv
# source djangoenv/bin/activate

# pip install django==4.2.4 psycopg2-binary==2.9.7

# python3 manage.py makemigrations standalone