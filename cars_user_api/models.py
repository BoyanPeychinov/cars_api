from django.db import models
from num2words import num2words

from auth_api.models import CustomUser
from cars_brand_api.models import CarBrand
from cars_models_api.models import CarModel
from common.soft_delete import SoftDeleteModel
from common.validators import odometer_max_value, check_user_age


class UserCar(SoftDeleteModel):
    """
    Create UserCar with relations to user, brand and brand models.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="cars")
    car_brand = models.ForeignKey(CarBrand, on_delete=models.PROTECT)
    car_model = models.CharField(max_length=50, null=True, blank=False)
    first_reg = models.DateField(null=True, blank=False)
    odometer = models.IntegerField(null=True, blank=False, validators=[odometer_max_value])
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Check if the user is adult

        age = self.user.age
        check_user_age(age)
        super(UserCar, self).clean()

    def __str__(self):
        if self.user.cars.count() > 0:
            car_count = num2words(self.user.cars.count(), to="ordinal")
            return f"{self.user.first_name} {self.user.last_name} {car_count}'s car"
        else:
            return "Car without owner"
