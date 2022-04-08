from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cars_brand_api.models import CarBrand
from cars_user_api.models import UserCar
from cars_user_api.serializers import UserCarSerializer, UserCarNoBrandSerializer
from common.filter import filter_obj


class UserCarListCreate(APIView):
    """
    List cars or filter them against url query parameters, which can be - brand, model, mileage, year,
    and the combinations of them.
    With POST is implemented logic for differentiation of creating user car with present brand and model,
    or with new ones.
    """

    serializer_class = UserCarSerializer

    def get(self, request):
        brand = request.query_params.get("brand")
        model = request.query_params.get("model")
        mileage = request.query_params.get("mileage")
        year = request.query_params.get("year")

        user_cars = filter_obj(UserCar, brand, model, mileage, year)

        serializer = self.serializer_class(user_cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        brand = request.data.get('car_brand', '')
        if type(brand) is str:
            brand.capitalize()
            brand = CarBrand.objects.filter(name=brand)
        else:
            brand = CarBrand.objects.filter(id=brand)

        if not brand.exists():
            serializer = UserCarNoBrandSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            brand_id = brand[0].id
            request.data["car_brand"] = brand_id
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCarGetUpdateDelete(APIView):

    serializer_class = UserCarSerializer

    def get(self, request, car_id):
        user_car = get_object_or_404(UserCar, id=car_id)
        serializer = self.serializer_class(user_car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, car_id):
        user_car = get_object_or_404(UserCar, id=car_id)
        serializer = self.serializer_class(user_car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors)

    def delete(self, request, car_id):
        user_car = get_object_or_404(UserCar, id=car_id)
        user_car.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
