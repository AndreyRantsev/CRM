from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "админ"),
        ("teacher", "учитель"),
        ("parent", "родитель"),
        ("student", "ученик")
    )

    roles = models.CharField(max_length=50, choices = ROLE_CHOICES, null=True)

    def __str__(self):
        return self.userName

