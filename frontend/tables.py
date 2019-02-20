import django_tables2 as tables
from teacher.models import Student

class StudentTable(tables.Table):
    class Meta:
        model = Student
        attrs = {'class': 'student table is-bordered is-fullwidth'}
    # tables.TemplateColumn("""a class="btn btn-info btn-sm" href="{% url 'training_update' record.id %}">Open</a>""")

