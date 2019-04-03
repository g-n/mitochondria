from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('teacher/', views.teacher_page, name='teacher'),
    path('student/', views.student_page, name='students')
]
