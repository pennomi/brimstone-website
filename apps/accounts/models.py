from enum import IntEnum

from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(IntEnum):
    Player = 0
    Contributor = 1
    Master = 2


ROLE_CHOICES = (
    (0, "Player"),
    (1, "Contributor"),
    (2, "Master"),
)


class User(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=0)
    image = models.ImageField(null=True, blank=True)
