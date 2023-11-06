# Python imports
import uuid
from django.contrib.auth.validators import UnicodeUsernameValidator
from datetime import datetime, timedelta
import pytz

# Django imports
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

# import custom foos, classes
from user.hash import hashing

# import constants
from user.constants import UserTelegramStatus

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

    telegram_password = models.CharField(max_length=32, null=True, default=None)
    telegram_password_expires = models.DateTimeField(default=None, null=True)

    def set_telegram_password_expires(self):
        ''' set time limit for actuality of telegram_password '''
        time_zone = pytz.UTC
        now = time_zone.localize(datetime.utcnow())
        self.telegram_password_expires = now + timedelta(minutes=5)
        self.save()

    def set_telegram_password(self):
        ''' generate and set random telegram_password '''
        self.telegram_password = hashing(
            user_id=self.id,
            password=self.username
        )[:31]
        self.set_telegram_password_expires()
        self.save()

    def __str__(self):
        return f"{self.username}"

    def __repr__(self):
        return f"{self.username}"
