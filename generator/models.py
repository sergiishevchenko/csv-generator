from django.db import models

class User(models.Model):
    email = models.CharField(max_length=30, verbose_name='Email пользователя')
    password = models.CharField(max_length=30, verbose_name='Пароль пользователя', default='None')
