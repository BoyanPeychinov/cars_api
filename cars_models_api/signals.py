from django.db.models.signals import post_delete
from django.dispatch import receiver

from cars_brand_api.models import CarBrand
from cars_models_api.models import CarModel


"""
Listening for delete signal from car brand, for the purpose of soft delete.
"""
@receiver(post_delete, sender=CarBrand)
def brand_models_deleted(sender, instance, **kwargs):
    brands = CarModel.objects.filter(car_brand_id=instance.id)
    for brand in brands:
        brand.soft_delete()