from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns

schema_view = get_schema_view(
    openapi.Info(
        title="Sunrise API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

admin.site.index_title = 'Sunrise'
admin.site.site_header = 'Sunrise Administration'
admin.site.site_title = 'Sunrise'


urlpatterns = [
    path('adminsunrise/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('main/', include('main.urls')),
    path('products/', include('products.urls')),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
)
