from django.shortcuts import render

from django.shortcuts import render
from teacher.models import Student
from .tables import StudentTable
from django_tables2 import RequestConfig
Student.objects.all()
def index(request):
    table  = StudentTable(Student.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'frontend/index.html', {'student': table})