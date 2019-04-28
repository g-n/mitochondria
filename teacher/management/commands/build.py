from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

import datetime
from teacher.models import Class, Student, Problem, ProblemSet, Game

import os
import pathlib
from django.core.management import call_command

import random


class Command(BaseCommand):
    def __init__(self):
        self.first_names = (
            open("teacher/fixtures/first_names.txt", "r").read().splitlines()
        )
        self.last_names = (
            open("teacher/fixtures/last_names.txt", "r").read().splitlines()
        )
        super().__init__()

    def make_classroom(self, user, name, problem_sets, num_students=10):
        c = Class.objects.create(classroom=name, user=user)

        for _ in range(num_students):
            jimmy = Student.objects.create(
                first_name=random.choice(self.first_names),
                last_name=random.choice(self.last_names),
                classroom=c,
            )
            jimmy.save()

            for problem_set in problem_sets:
                for _ in range(random.randint(0, 5)):
                    Game.objects.create(
                        score=random.randint(5, 20),
                        problemset=problem_set,
                        student=jimmy,
                        date=datetime.date.today()
                        - datetime.timedelta(days=random.randint(0, 10)),
                    ).save()

        c.save()

    def gen_problem(self, lim, min=0):
        num1 = random.randint(min, lim)
        correct = random.randint(min + 1, lim + 1)

        answer = num1 + correct

        while True:
            incorrect = random.randint(min + 1, lim + 1)
            if incorrect != correct and incorrect >= 0:
                break

        return {
            "target": "{}+_={}".format(str(num1), str(answer)),
            "correct": str(correct),
            "incorrect": str(incorrect),
        }

    def handle(self, *args, **options):
        print(os.getcwd())
        if os.path.exists("db.sqlite3"):
            os.remove("db.sqlite3")
        for x in pathlib.Path("teacher/migrations/").iterdir():
            if not x.is_dir() and x.name != "__init__.py":
                os.remove(str(x))
        call_command("makemigrations", interactive=False)
        call_command("migrate", interactive=False)

        User.objects.create_superuser(
            username="admin", password="admin", email="a"
        ).save()

        u1 = User.objects.create_user(username="teacher", password="teacher", email="b")
        u1.save()

        user2 = User.objects.create_user(username="t2", password="t2", email="b")
        user2.save()

        # first_grade = Class.objects.create(classroom="first grade", user=u1)
        # first_grade.save()
        #
        # second_grade = Class.objects.create(classroom="first grade", user=user2)
        # second_grade.save()

        # subtraction = ProblemSet.objects.create(set_name="subtraction", user=u1)

        easy_addition = ProblemSet.objects.create(set_name="easy addition", user=u1)
        easy_addition.save()
        for _ in range(20):
            Problem.objects.create(
                set_name=easy_addition, **self.gen_problem(10)
            ).save()

        big_number = ProblemSet.objects.create(set_name="large numbers", user=u1)
        big_number.save()
        for _ in range(15):
            Problem.objects.create(
                set_name=big_number, **self.gen_problem(500, 100)
            ).save()

        self.make_classroom(u1, "first grade", [easy_addition, big_number])
        self.make_classroom(u1, "second grade", [easy_addition, big_number])

        # Problem.objects.create(target="1+_=2", correct="1", incorrect="2", set_name=easy_addition).save()
        # Problem.objects.create(target="2+_=4", correct="2", incorrect="0", set_name=easy_addition).save()

        # jimmy = Student.objects.create(first_name="Alex", last_name="Chillin", classroom=first_grade)
        # jimmy.save()
        # timmy = Student.objects.create(first_name="Timmy", last_name="Youngin", classroom=first_grade)
        # timmy.save()
        #
        # Game.objects.create(score=20, problemset=easy_addition, student=jimmy, date=datetime.date.today()).save()
        # Game.objects.create(score=10, problemset=easy_addition, student=jimmy, date=datetime.date.today()).save()
        # Game.objects.create(score=5, problemset=easy_addition, student=timmy, date=datetime.date.today()).save()
