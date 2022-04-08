from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from common.soft_delete import SoftDeleteModel
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin, SoftDeleteModel):
    """
    Custom user class, overriding django user class. Email field is used for the account instead of username.
    Task specifications impose Custom User without Profile model, so User will have fields not related to authorization.
    """

    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False
    )

    is_staff = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # Profile fields

    first_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    age = models.IntegerField(
        null=True,
        blank=False
    )

    phone_number = models.IntegerField(
        null=True,
        blank=True,
    )

    user_image = models.ImageField(
        upload_to='user_img',
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"