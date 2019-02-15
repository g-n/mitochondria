from django.test import TestCase, override_settings, TransactionTestCase
from .models import Student

class TeacherTest(TransactionTestCase):
    def test_add(self):
        a = Student(first_name='billy', last_name='chillins')
        a.save()

