from django.db import models

from common.soft_delete import SoftDeleteModel


class CarBrand(SoftDeleteModel):
    name = models.CharField(max_length=20, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
