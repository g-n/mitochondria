from django.contrib import admin
from django.urls import path, include
from teacher.urls import urlpatterns as turl
from frontend.urls import urlpatterns as furl


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teacher.urls')),
    path('', include('frontend.urls')),
]
