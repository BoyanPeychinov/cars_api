from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from auth_api.serializers import RegisterSerializer, LoginSerializer, CustomUserSerializer

User = get_user_model()


class RegisterView(GenericAPIView):

    serializer_class = RegisterSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):

    serializer_class = LoginSerializer


    def post(self, request):
        email = request.data.get('email', None)

        user = User.objects.get(email=email)

        if user:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'message': "Invalid email or password, try again"}, status=status.HTTP_401_UNAUTHORIZED)


class ListUsers(APIView):
    """
    Used for listing all users, and filter against url query parameters. Possible filters are: brand, model, age,
    every combination of the three.
    """

    serializer_class = CustomUserSerializer

    def get(self, request):
        brand = request.query_params.get("brand")
        model = request.query_params.get("model")
        age = request.query_params.get("age")
        users = User.objects.all()

        if brand:
            users = users.filter(cars__car_brand__name=brand)
        if model:
            users = users.filter(cars__car_model=model)
        if age and age.endswith("gt"):
            users = users.filter(age__gte=age[:-2])
        elif age and age.endswith("lt"):
            users = users.filter(age__lte=age[:-2])

        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetEditDeleteUser(APIView):

    serializer_class = CustomUserSerializer

    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user_car = get_object_or_404(User, id=pk)
        serializer = self.serializer_class(user_car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors)

    def delete(self, request, pk):
        user_car = get_object_or_404(User, id=pk)
        user_car.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)