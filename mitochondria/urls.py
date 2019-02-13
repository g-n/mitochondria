from django.contrib import admin
from django.urls import path
from teacher.urls import urlpatterns as turl

urlpatterns = [
    path('admin/', admin.site.urls),
] + turl
