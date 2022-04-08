from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cars_api.views import overview_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', overview_page, name='overview'),
    path('api/auth/', include('auth_api.urls')),
    path('api/cars/', include('cars_user_api.urls')),
    path('api/brands/', include('cars_brand_api.urls')),
    path('api/models/', include('cars_models_api.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)