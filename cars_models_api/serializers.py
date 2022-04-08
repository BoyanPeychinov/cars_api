from rest_framework import serializers

from cars_models_api.models import CarModel
from common.validators import check_first_char_is_upper


class CarModelsSerializer(serializers.ModelSerializer):
    """
    Transform data for car model and make simple validations.
    """

    name = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = CarModel
        fields = ('id', 'name', 'car_brand')

    def validate(self, data):
        name = data.get("name", None)
        if name:
            # if not name[0].isupper() and name[0].isalpha():
            #     raise serializers.ValidationError("Name must start with capital letter")
            check_first_char_is_upper(name)

            if CarModel.objects.filter(name=name).exists():
                raise serializers.ValidationError("This model already exists")
            return data

