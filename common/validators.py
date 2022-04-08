from django.core.exceptions import ValidationError


def odometer_max_value(value):
    max_value = 999999

    if value >= max_value:
        raise ValidationError("Incorrect kilometers. Try again!")


def check_user_age(value):
    min_age = 18

    if value < min_age:
        raise ValidationError("You can't posses car, must have 18 years at least!")


def check_first_char_is_upper(value):
    if not value[0].isupper() and value[0].isalpha():
        raise ValidationError("Name must start with capital letter")