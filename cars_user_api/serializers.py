from rest_framework import serializers

from cars_brand_api.models import CarBrand
from cars_user_api.models import UserCar
from common.validators import odometer_max_value, check_user_age


class UserCarSerializer(serializers.ModelSerializer):
    car_model = serializers.CharField(max_length=50, required=True)
    odometer = serializers.IntegerField(required=True)

    class Meta:
        model = UserCar
        fields = ('id', 'user', 'car_brand', 'car_model', 'first_reg', 'odometer',)

    def validate(self, data):
        odometer = data.get('odometer')
        user_age = data.get('user').age
        if odometer:
            odometer_max_value(odometer)
        if user_age:
            check_user_age(user_age)
        return data

    def create(self, validated_data):
        model = validated_data.pop('car_model').casefold().capitalize()
        brand = validated_data.pop('car_brand')

        if model and type(model) == str and not brand.models.filter(name=model):
            brand.models.create(name=model)

        return UserCar.objects.create(car_brand=brand, car_model=model, **validated_data)


class UserCarNoBrandSerializer(serializers.ModelSerializer):
    """
    Transform data for user car, if the input brand is not present in the db, it's created with the input model.
    Simple validations - if the car mileage is 1 000 000 or above
    and if the user is adult.
    """

    car_brand = serializers.CharField(max_length=50, required=True)
    car_model = serializers.CharField(max_length=50, required=True)
    odometer = serializers.IntegerField(required=True)

    class Meta:
        model = UserCar
        fields = ('id', 'user', 'car_brand', 'car_model', 'first_reg', 'odometer',)

    def validate(self, data):
        odometer = data.get('odometer')
        user_age = data.get('user').age
        if odometer:
            odometer_max_value(odometer)
        if user_age:
            check_user_age(user_age)

        return data

    def create(self, validated_data):
        model = validated_data.pop('car_model')
        brand = validated_data.pop('car_brand')
        new_brand = CarBrand.objects.create(name=brand)
        new_brand.save()
        new_brand.models.create(name=model)
        new_brand.save()
        validated_data['car_brand'] = new_brand
        validated_data['car_model'] = model
        return UserCar.objects.create(**validated_data)