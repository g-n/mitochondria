from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from .models import Student, Game, ProblemSet, Class

from .serializers import (
    ClassesSerializer,
    StudentSerializer,
    ProblemSetSerializer,
    GameSerializer,
)

from .filters import IsOwnerFilterBackend
from .permissions import IsOwnerOfObject


class BaseTeacherView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    permission_classes = (IsAdminUser | (IsAuthenticated & IsOwnerOfObject),)
    filter_backends = (IsOwnerFilterBackend,)
    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
    )


class StudentViewSet(BaseTeacherView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # lookup_field = "classroom"


class ClassesViewSet(BaseTeacherView):
    queryset = Class.objects.all()
    serializer_class = ClassesSerializer
    lookup_field = "class_name"


class GameViewSet(BaseTeacherView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = "student"


class ProblemSetViewSet(BaseTeacherView):
    queryset = ProblemSet.objects.all()
    serializer_class = ProblemSetSerializer
    lookup_field = "set_name"

    def list(self, request, **kwargs):
        return Response(self.get_queryset().values_list(self.lookup_field, flat=True))
