from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

import datetime
from teacher.models import Class, Student, Problem, ProblemSet, Game

import os
import pathlib
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(os.getcwd())
        if os.path.exists("db.sqlite3"):
            os.remove("db.sqlite3")
        for x in pathlib.Path("teacher/migrations/").iterdir():
            if not x.is_dir() and x.name != "__init__.py":
                os.remove(str(x))
        call_command("makemigrations", interactive=False)
        call_command("migrate", interactive=False)

        User.objects.create_superuser(username="admin", password="admin", email="a").save()

        u1 = User.objects.create_user(username="teacher", password="teacher", email="b")
        u1.save()
        first_grade = Class.objects.create(classroom="first grade", user=u1)
        first_grade.save()
        easy_addition = ProblemSet.objects.create(set_name="easy addition", user=u1)
        easy_addition.save()
        Problem.objects.create(target="1+_=2", correct="1", incorrect="2", set_name=easy_addition).save()
        Problem.objects.create(target="2+_=4", correct="2", incorrect="0", set_name=easy_addition).save()
        jimmy = Student.objects.create(first_name="Alex", last_name="Chillin", classroom=first_grade)
        jimmy.save()
        Game.objects.create(score=20, problemset=easy_addition, student=jimmy, date=datetime.date.today()).save()
        Game.objects.create(score=10, problemset=easy_addition, student=jimmy, date=datetime.date.today()).save()

        timmy = Student.objects.create(first_name="Timmy", last_name="Youngin", classroom=first_grade)
        timmy.save()
        Game.objects.create(score=5, problemset=easy_addition, student=timmy, date=datetime.date.today()).save()

        User.objects.create_user(username="t2", password="t2", email="b").save()
