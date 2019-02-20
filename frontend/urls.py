from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('students/', views.student_page, name='teacher'),
]

