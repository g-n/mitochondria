from django.test import TestCase, override_settings, TransactionTestCase
from .models import Student



from django.test.runner import DiscoverRunner
import dj_database_url
# def test_setup():
#     TestCase.modify_settings()
#
#
# TestCase.setUp = test_setup()


class TeacherTest(TransactionTestCase):
    databases={'testdb'}
    def test_add(self):
        a = Student(first_name='billy', last_name='chillins')
        a.save()




# python manage.py test --testrunner teacher.tests.TestRunner
# class TestRunner(TestCase):
#     def setup_databases(self, **kwargs):
#         TestCase
#         pass
#     def teardown_databases(self, old_config, **kwargs):
#         pass

