from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField, ArrayField

class Student(User):
    class Meta:
        proxy = True

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    username = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=15, null=True)

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name, self.username, self.password)
