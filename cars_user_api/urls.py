from django.urls import path

from cars_user_api.views import UserCarListCreate, UserCarGetUpdateDelete

urlpatterns = [
    path('', UserCarListCreate.as_view(), name='car-list-create'),
    path('<int:car_id>', UserCarGetUpdateDelete.as_view(), name='car-get-put-del'),
    # path('?brand=brand_name', ListCarsByBrand.as_view(), name='cars-by-brand'),
]