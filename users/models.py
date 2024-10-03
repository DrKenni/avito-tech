from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    is_active = models.BooleanField(default=False, verbose_name='Активация')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
