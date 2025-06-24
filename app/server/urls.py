from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

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
    path('api/v1/core_auth/', include("core_auth.v1.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
