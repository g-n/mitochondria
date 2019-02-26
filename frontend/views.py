from django.shortcuts import render
from teacher.models import Student
from teacher.serializers import StudentSerializer


def index(request):
    return render(request, 'frontend/index.html')

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
                s.delete()
                print('dropped', s.first_name, s.last_name, s.id)
        except Exception as e:
            print('cant drop student')

    queryset = Student.objects.all().order_by('last_name','first_name')
    return render(request, 'frontend/students.html', {'student': queryset})
