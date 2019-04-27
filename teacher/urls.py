from django.urls import include, path
from rest_framework import routers

from .views import StudentViewSet, ClassesViewSet, GameViewSet, ProblemSetViewSet


router = routers.DefaultRouter()
router.register(r"classes", ClassesViewSet, base_name="classroom")
router.register(r"problemsets", ProblemSetViewSet)
router.register(r"students", StudentViewSet, basename="students")
router.register(r"games", GameViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("accounts/", include("django.contrib.auth.urls")),
]
