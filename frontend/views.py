
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
    serializer_class = Student
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.POST)
        print('fucky')

        if serializer.is_valid():
            if request.POST['do']== 'add':
                studen = Student.objects.create(**serializer.data)
                studen.save()
        try:
            if request.POST['do'] == 'drop':
                s = Student.objects.get(id=request.POST['id'])
                print(s)
                s.delete()
                # s.save()
        except Exception as e:
            print('error')


    # table = StudentTable(Student.objects.all(), exclude='id', order_by='last_name', )
    # RequestConfig(request).configure(table)
    # return render(request, 'frontend/students.html', {'student': table})
    queryset = Student.objects.all().order_by('last_name','first_name')
    return render(request, 'frontend/students.html', {'student': queryset})
