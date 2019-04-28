from django.db import models
from django.contrib import auth

class Class(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    classroom = models.CharField(max_length=30)

    def __str__(self):
        return self.classroom


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    classroom = models.ForeignKey(
        "teacher.Class", on_delete=models.CASCADE, related_name="students"
    )

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)

    class Meta:
        unique_together = ("last_name", "first_name", "classroom")


class Game(models.Model):
    score = models.IntegerField()
    date = models.DateField()
    student = models.ForeignKey(
        "teacher.Student", on_delete=models.CASCADE, related_name="scores"
    )
    problemset = models.ForeignKey(
        "teacher.ProblemSet", on_delete=models.CASCADE, related_name="problemset"
    )


class ProblemSet(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    set_name = models.CharField(max_length=30)

    def __str__(self):
        return self.set_name


class Problem(models.Model):
    target = models.CharField(max_length=50)
    correct = models.CharField(max_length=50)
    incorrect = models.CharField(max_length=50)
    set_name = models.ForeignKey(
        "teacher.ProblemSet", models.CASCADE, related_name="problems"
    )
