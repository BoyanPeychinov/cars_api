from rest_framework import serializers

from cars_brand_api.models import CarBrand
from common.validators import check_first_char_is_upper


class CarBrandSerializer(serializers.ModelSerializer):
    """
       Transform data for car brand and make simple validations - name first letter is capitalized.
    """

    name = serializers.CharField(max_length=20, required=True)
    models = serializers.StringRelatedField(many=True)

    class Meta:
        model = CarBrand
        fields = ('id', 'name', 'models',)
        depth = 1

    def validate(self, data):
        name = data.get("name", None)
        if name:
            # if not name[0].isupper() and name[0].isalpha():
            #     raise serializers.ValidationError("Name must start with capital letter")
            check_first_char_is_upper(name)
        return data
