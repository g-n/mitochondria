from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets

from teacher.models import Problem, ProblemSet, Roster, Teacher


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'username', 'email')


class RosterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Roster
        fields = '__all__'

class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'
#
class ProblemSetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProblemSet
        fields = '__all__'
