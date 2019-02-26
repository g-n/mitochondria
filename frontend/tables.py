import django_tables2 as tables
from teacher.models import Student

class StudentTable(tables.Table):
    class Meta:
        model = Student
        attrs = {'class': 'student table is-bordered is-fullwidth'}
        fields = ['first_name', 'last_name', 'delete']
    delete = tables.TemplateColumn(template_name='frontend/delete_button.html')
    delete.attrs = {
        'th':{'id':'delete_col'},
        'tr':{'id':'delete_row'}
                    }


