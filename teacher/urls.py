from django.urls import include, path
from rest_framework import routers
from teacher.views import UserViewSet, GroupViewSet, StudentViewSet, StudentListCreate

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'student', StudentViewSet)
# router.register(r'class', StudentListCreate)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/class/', StudentListCreate.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('', include('frontend.urls')),
]