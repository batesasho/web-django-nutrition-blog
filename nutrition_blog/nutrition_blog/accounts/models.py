from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from nutrition_blog.accounts.managers import AppUserManager
from nutrition_blog.accounts.validators import validate_only_letters, ValidateMaxSizeMB


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    # extend with a new field of email that is unique and a must
    email = models.EmailField(
            unique = True,

    )

    date_joined = models.DateTimeField(
            auto_now_add = True,
    )

    # all new users can not have stuff privilege
    is_staff = models.BooleanField(
            default = False,
    )

    is_active = models.BooleanField(
            default = True
    )
    # is_active = models.BooleanField(default = True)

    # overwrite what should be the registration method based on -> change from username to email
    USERNAME_FIELD = 'email'

    # define managers in order to all manage.py commands work i.e create superuser, administration etc.
    objects = AppUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 20
    AGE_MIN_VALUE = 0
    AGE_MAX_VALUE = 100

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(

            null = True,
            blank = True,
            max_length = FIRST_NAME_MAX_LENGTH,
            validators = (
                    MinLengthValidator(FIRST_NAME_MIN_LENGTH),
                    validate_only_letters,
            )
    )

    last_name = models.CharField(
            max_length = LAST_NAME_MAX_LENGTH,
            validators = (
                    MinLengthValidator(LAST_NAME_MIN_LENGTH),
                    validate_only_letters,
            ),
            null = True,
            blank = True,
    )

    age = models.PositiveIntegerField(
            validators = (
                    MinValueValidator(AGE_MIN_VALUE),
                    MaxValueValidator(AGE_MAX_VALUE),
            ),
            null = True,
            blank = True,
    )

    profile_image = models.ImageField(
            upload_to = 'profile_photo/',
            default = 'default.jpg',
            validators = (
                    ValidateMaxSizeMB,
            ),

    )
    gender = models.CharField(
            max_length = max(len(x) for x, _ in GENDERS),
            choices = GENDERS,
            null = True,
            blank = True,
            default = DO_NOT_SHOW,
    )

    user = models.OneToOneField(
            AppUser,
            on_delete = models.CASCADE,
            primary_key = True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


from .signals import *
