from django.db import models

from cars_brand_api.models import CarBrand
from safedelete.models import SafeDeleteModel

from common.soft_delete import SoftDeleteModel


class CarModel(SoftDeleteModel):

    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name="models")
    name = models.CharField(max_length=50, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


