from django.urls import path, include
from students import views

from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'student', views.StudentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('student/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),
]
