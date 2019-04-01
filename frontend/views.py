from django.shortcuts import render
from students.models import Student
from teacher.models import Teacher
from teacher.serializers import TeacherSerializer
from students.serializers import StudentSerializer


def index(request):
    return render(request, 'frontend/index.html')

def teacher_page(request):
    serializer_class = Student
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.POST)
        print('fucky')

        if serializer.is_valid():
            if request.POST['do']== 'add':
                teach = Student.objects.create(**serializer.data)
                teach.save()
        try:
            if request.POST['do'] == 'drop':
                t = Student.objects.get(url=request.POST['id'])
                t.delete()
                print('dropped',  t.id, t.first_name, t.last_name)
        except Exception as e:
            print('cant drop student')

    queryset = Student.objects.all().order_by('id')
    return render(request, 'frontend/teacher.html', {'student': queryset})


def student_page(request):
    serializer_class = Student
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.POST)

        if serializer.is_valid():
            if request.POST['do']== 'add':
                studen = Student.objects.create(**serializer.data)
                studen.save()
        try:
            if request.POST['do'] == 'drop':
                s = Student.objects.get(id=request.POST['id'])
                s.delete()
                print('dropped', s.first_name, s.last_name, s.id)
        except Exception as e:
            print('cant drop student')

    queryset = Student.objects.all().order_by('id')
    return render(request, 'frontend/students.html', {'student': queryset})
