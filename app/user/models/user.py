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
    first_name = last_name = is_superuser = is_staff = None

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

    password = models.CharField(
        max_length=4096,
        validators=[
            MinLengthValidator(
                limit_value=7,
                message="Password must be at least 7 characters long."
            )
        ]
    )

    created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    def validate_password(self, password):
        ''' проверки для пароля '''
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                "Password must contain at least one digit.",
                code="password_no_digit"
            )

        if not any(char.isupper() for char in password):
            raise ValidationError(
                "Password must contain at least one uppercase letter.",
                code="password_no_uppercase"
            )

        if not any(char.islower() for char in password):
            raise ValidationError(
                "Password must contain at least one lowercase letter.",
                code="password_no_lowercase"
            )

    def save(self, *args, **kwargs):
        ''' вызов метода  '''
        self.validate_password(self.password)
        super().save(*args, **kwargs)        

    def __str__(self):
        return f"{self.username}"

    def __repr__(self):
        return f"{self.username}"
