from django.contrib.auth.models import AbstractUser
from django.db import models


ROLE_CHOICES = (
    (0, "Player"),
    (1, "Contributor"),
    (2, "Master"),
)


class User(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=0)
