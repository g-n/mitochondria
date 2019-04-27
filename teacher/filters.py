from django.contrib.auth.models import User
from django.core.exceptions import FieldError
from rest_framework.filters import BaseFilterBackend
from .models import Class, Problem, ProblemSet, Student


class IsOwnerFilterBackend(BaseFilterBackend):
    """
    Filters a viewset so a teacher only sees their problemsets, class rosters, etc
    """

    def filter_queryset(self, request, queryset, view):
        user: User = request.user
        if user.is_superuser:
            return queryset
        if user.is_anonymous:
            return []
        else:
            print(view.lookup_field)
            try:
                return queryset.filter(user=user)
            except FieldError:
                try:
                    return queryset.filter(classroom__in=Class.objects.filter(user=user))
                except FieldError:
                    try:
                        return queryset.filter(problems__in=ProblemSet.objects.filter(user=user))
                    except FieldError:
                        return queryset.filter(student__in=Student.objects.all())
