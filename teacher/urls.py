from django.urls import include, path
from rest_framework import routers
from teacher.views import UserViewSet, GroupViewSet, StudentViewSet, ProblemSetViewSet, ProblemViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'student', StudentViewSet)
router.register(r'problemset', ProblemSetViewSet)
router.register(r'problem', ProblemViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]