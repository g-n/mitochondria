
from .models import Student
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'username', 'password')
