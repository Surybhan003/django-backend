from django.db import models
# from .models import *
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    message=models.TextField(max_length=500)

    def __str__(self)->str:
        return self.name
# django-admin startproject portfolio_platform   
# cd myproject
# Set-ExecutionPolicy Unrestricted -Scope Process
# C:\Users\mourya\Desktop\Django\venv\Scripts\Activate.ps1
# C:\Users\mourya\Desktop\Django\myproject\venv\Scripts\activate