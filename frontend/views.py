
from django.shortcuts import render
from teacher.models import Student
from .tables import StudentTable
from django_tables2 import RequestConfig
from django.contrib.auth.models import User
from teacher.serializers import StudentSerializer


def index(request):
    table  = StudentTable(Student.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'frontend/index.html', {'student': table})

def student_page(request):
    queryset = User.objects.all()
    serializer_class = Student

    if request.method == 'GET':
        table = StudentTable(Student.objects.all(), exclude='id')
        RequestConfig(request).configure(table)
        return render(request, 'frontend/students.html', {'student': table})

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.POST)
        if serializer.is_valid():
            studen = Student.objects.create(**serializer.data)
            studen.save()
        table = StudentTable(Student.objects.all(), exclude='id')
        RequestConfig(request).configure(table)
        return render(request, 'frontend/students.html', {'student': table})
