from django.test import TestCase, override_settings, TransactionTestCase, Client
import requests
from .models import Student

class TeacherTest(TestCase):
    def test_working_db(self):
        Student(first_name='billy', last_name='chillins').save()
        Student(first_name='jon', last_name='mcchill', nick='a').save()
        TestCase.assertEqual(self, Student.objects.count(), 2)

