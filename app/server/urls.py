from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Django lab API",
        default_version='v1',
        description="Easy and fast api for tests",
        terms_of_service="regisdeveloper.com",
        contact=openapi.Contact(email="regisdev@gmail.com"),
        license=openapi.License(name="Regis License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/core/', include("core.v1.urls")),
    path('api/v1/core_image/', include("core_image.v1.urls")),
    path('', schema_view.with_ui('swagger', cache_timeout=0)),  # Usando Swagger UI
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
