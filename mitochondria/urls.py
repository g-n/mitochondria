from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(title="Math Mart 3 API", default_version="v1"), public=True, permission_classes=(permissions.AllowAny,)
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("", include("teacher.urls")),
    path("api/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("accounts/", include("django.contrib.auth.urls")),
]
