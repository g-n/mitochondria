from django.contrib import admin
from django.urls import path, include
from teacher.urls import urlpatterns as turl
from frontend.urls import urlpatterns as furl
from students.urls import urlpatterns as surl


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('teacher.urls')),
    path('', include('frontend.urls')),
    path('', include('students.urls')),
]
