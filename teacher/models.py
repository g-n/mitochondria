from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField, ArrayField

class Teacher(User):
    class Meta:
        proxy = True

class ProblemSet(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # data =  ArrayField(ArrayField(models.CharField(max_length=30), size=3))
    #data = models.CharField(max_length=50000)
    f = JSONField()
    # data =  ArrayField(JSONField())
    def __str__(self):
        return self.name


class Roster(models.Model):
    roster_name = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    problem_sets = models.ManyToManyField(ProblemSet, blank=True)
    # students = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.roster_name

class Problem(models.Model):
    target = models.CharField(max_length=30)
    correct = models.CharField(max_length=30)
    incorrect = models.CharField(max_length=30)
    # problem_set = models.ForeignKey(ProblemSet, on_delete=models.CASCADE)
