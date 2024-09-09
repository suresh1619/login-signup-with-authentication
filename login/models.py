from django.db import models

# Create your models here.
class login_details(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
class Signup(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
