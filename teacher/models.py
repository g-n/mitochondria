from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    nick = models.CharField(max_length=50, blank=True, verbose_name='Nickname')
