from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from teacher.serializers import UserSerializer, GroupSerializer
from teacher.serializers import StudentSerializer
from teacher.models import Student


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
