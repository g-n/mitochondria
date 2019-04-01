from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from teacher.views import TeacherViewSet, RosterViewSet, ProblemList, ProblemViewSet
router = routers.DefaultRouter()
router.register(r'teacher', TeacherViewSet)
router.register(r'roster', RosterViewSet)
router.register(r'problemsets', ProblemList)



urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
