from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cars_models_api.models import CarModel
from cars_models_api.serializers import CarModelsSerializer


class CarModelsListCreate(APIView):

    serializer_class = CarModelsSerializer

    def get(self, request):
        car_models = CarModel.objects.all()
        serializer = self.serializer_class(car_models, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarModelGetUpdateDelete(APIView):

    serializer_class = CarModelsSerializer

    def get(self, request, model_id):
        car_model = get_object_or_404(CarModel, id=model_id)
        serializer = self.serializer_class(car_model)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, model_id):
        car_model = get_object_or_404(CarModel, id=model_id)
        serializer = self.serializer_class(car_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors)

    def delete(self, request, model_id):
        car_model = get_object_or_404(CarModel, id=model_id)
        car_model.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)