from django.db.models.signals import post_delete
from django.dispatch import receiver

from auth_api.models import CustomUser
from cars_user_api.models import UserCar


"""
Listening for delete signal from user, for the purpose of soft delete.
"""
@receiver(post_delete, sender=CustomUser)
def user_cars_deleted(sender, instance, **kwargs):
    cars = UserCar.objects.filter(user_id=instance.id)
    for car in cars:
        car.soft_delete()