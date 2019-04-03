from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer
