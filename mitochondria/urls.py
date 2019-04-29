from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
import pandas as pd

from teacher import models

schema_view = get_schema_view(
    openapi.Info(title="Math Mart 3 API", default_version="v1"),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)


def index(request):
    if not request.user.is_anonymous:
        models.Student.objects.all().values_list()
        user = request.user
        problemsets = models.ProblemSet.objects.filter(user=user)
        problems = models.Problem.objects.filter(set_name__in=problemsets)

        classrooms = models.Class.objects.filter(user=user)
        seta = []
        for classroom in classrooms:
            students = models.Student.objects.filter(classroom=classroom)
            for student in students:
                for problemset in problemsets:
                    ps = problemset.problems.all()

                    games = models.Game.objects.filter(student=student, problemset=problemset)
                    for game in games:
                        seta.append(
                            [
                                classroom.classroom,
                                student.first_name,
                                student.last_name,
                                problemset.set_name,
                                len(ps),
                                game.score,
                                str(int(round(game.score / len(ps), 2) * 100)) + "%",
                                game.date,
                            ]
                        )
        df = pd.DataFrame(seta, columns=["Class", "First", "Last", "Problemset", "# total", "Score", "%", "Date"])
        df = df.sort_values(["Class", "Problemset", "Last", "Date"])

        pa = []
        for x in problemsets:
            for y in x.problems.filter(set_name=x):
                pa.append([x.set_name, y.target, y.correct, y.incorrect])
        sf = pd.DataFrame(pa, columns=["Problemset", "Target", "Correct", "Incorrect"]).sort_values(["Problemset"])
        context = {
            "scores": df.to_html(index=False, classes=["table-striped"]),
            "problems": sf.to_html(index=False, classes=["table-striped"]),
        }
    else:
        context = {"scores": "", "problems": ""}

    return render(request, "home.html", context)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("", include("teacher.urls")),
    path("api/", schema_view.with_ui("swagger", cache_timeout=0), name="api"),
    path("accounts/", include("django.contrib.auth.urls")),
]
