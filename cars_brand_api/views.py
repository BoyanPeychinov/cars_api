from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cars_brand_api.models import CarBrand
from cars_brand_api.serializers import CarBrandSerializer


class CarBrandListCreate(APIView):
    serializer_class = CarBrandSerializer

    def get(self, request):
        car_brands = CarBrand.objects.all()
        serializer = self.serializer_class(car_brands, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarBrandGetUpdateDelete(APIView):
    serializer_class = CarBrandSerializer

    def get(self, request, brand_id):
        car_brand = get_object_or_404(CarBrand, id=brand_id)
        serializer = self.serializer_class(car_brand)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, brand_id):
        car_brand = get_object_or_404(CarBrand, id=brand_id)
        serializer = self.serializer_class(car_brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors)

    def delete(self, request, brand_id):
        car_brand = get_object_or_404(CarBrand, id=brand_id)
        car_brand.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

