from django.urls import path

from cars_models_api.views import CarModelsListCreate, CarModelGetUpdateDelete

urlpatterns = [
    path('', CarModelsListCreate.as_view(), name="model-list-create"),
    path('<int:model_id>', CarModelGetUpdateDelete.as_view(), name="model-get-put-del"),
]