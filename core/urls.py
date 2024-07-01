from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import  SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/', include('rest_framework.urls')),
    path('api/',include('port.api.urls')),
    path('',include('port.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)