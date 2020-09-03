from django.contrib.auth.models import AbstractUser  # to create custom user
from django.db import models


class CustomUser(AbstractUser):
    ROLES = (("0", "Admin"), ("1", "Journalist"), ("2", "Guest"))
    role = models.CharField(max_length=1, choices=ROLES, default="2")
    email = models.EmailField(
        verbose_name="email address", max_length=255, unique=True,)
    age = models.PositiveIntegerField(null=True, blank=True)

    # when admin/ opens in browser the sign in comes with email not username
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = "username", "role", "first_name", "last_name", "age"

    def __str__(self):
        return self.username
