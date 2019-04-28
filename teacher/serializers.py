from rest_framework import serializers
from .models import Problem, ProblemSet, Class, Student, Game


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ("target", "correct", "incorrect")


class ProblemSetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    problems = ProblemSerializer(many=True)

    class Meta:
        model = ProblemSet
        fields = ("user", "set_name", "problems")


class GameSerializer(serializers.ModelSerializer):
    problemset_name = serializers.StringRelatedField(source="problemset")

    class Meta:
        model = Game
        fields = ("problemset_name", "date", "score")


class StudentSerializer(serializers.ModelSerializer):
    scores = GameSerializer(many=True)

    class Meta:
        model = Student
        fields = ("first_name", "last_name", "scores", "id")


class ClassesSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)

    def create(self, validated_data):
        tracks_data = validated_data.pop("students")
        _class = Class.objects.create(**validated_data)
        for track_data in tracks_data:
            Student.objects.create(classroom=_class, **track_data)
        return _class

    class Meta:
        model = Class
        fields = ("students", "classroom")
