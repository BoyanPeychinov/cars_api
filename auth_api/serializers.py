from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, max_length=128, min_length=6, write_only=True)
    age = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "password", "age", "first_name", "last_name", "phone_number", "user_image")

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password',)


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "age", "user_image", "cars")