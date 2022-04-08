from django.urls import path

from cars_brand_api.views import CarBrandListCreate, CarBrandGetUpdateDelete

urlpatterns = [
    path('', CarBrandListCreate.as_view(), name="brand-list-create"),
    path('<int:brand_id>', CarBrandGetUpdateDelete.as_view(), name="brand-get-put-del"),
]