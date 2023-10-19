# Python imports
import uuid
from django.contrib.auth.validators import UnicodeUsernameValidator

# Django imports
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError


class User(AbstractUser):
    ''' database model of user '''
    REQUIRED_FIELDS = []
    first_name = last_name = None

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "users"
        ordering = ['-created']
        indexes = [
            models.Index(fields=['username'], name='username_index')
            ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        null=True,
        error_messages={"unique": "Username exists"},
    )

    email = models.EmailField(
        null=True,
        unique=True,
        verbose_name="User's email",
        error_messages={"unique": "Email exists"}
    )

    password = models.CharField(max_length=4096)

    created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    def __str__(self):
        return f"{self.username}"

    def __repr__(self):
        return f"{self.username}"
