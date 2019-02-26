from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('teacher/', views.student_page, name='teacher'),
    # path('students/', views.student_page, name='teacher'),
]

