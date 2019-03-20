from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    nick = models.CharField(max_length=50, blank=True, verbose_name='Nickname')


class Problem(models.Model):
    first = models.CharField(max_length=30)
    second = models.CharField(max_length=30)
    target = models.CharField(max_length=30)
    correct = models.IntegerField()


class ProblemSet(models.Model):
    name = models.CharField(max_length=30)
    problem_set = models.ForeignKey(Problem, on_delete=models.CASCADE)

