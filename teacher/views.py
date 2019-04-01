from rest_framework import viewsets

#from teacher.models import Student,  Problem, ProblemSet, Roster, Teacher
#from teacher.serializers import TeacherSerializer, StudentSerializer, RosterSerializer, ProblemSerializer, ProblemSetSerializer
from teacher.models import Problem, ProblemSet, Roster, Teacher
from teacher.serializers import TeacherSerializer, RosterSerializer, ProblemSerializer, ProblemSetSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('-date_joined')
    serializer_class = TeacherSerializer

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all().order_by('last_name','first_name')
#     serializer_class = StudentSerializer

class RosterViewSet(viewsets.ModelViewSet):
    queryset = Roster.objects.all()
    serializer_class = RosterSerializer

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

class ProblemList(viewsets.ModelViewSet):
    queryset = ProblemSet.objects.all()
    serializer_class = ProblemSetSerializer


