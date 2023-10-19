# DRF imports
from rest_framework import serializers

# import models
from user.models.user import User


class UserSerializer(serializers.ModelSerializer):
    ''' serializer for get objects of Product model'''

    email = serializers.EmailField(
        trim_whitespace=True,
        label='Email'
    )
    username = serializers.CharField(
        trim_whitespace=True,
        label='Username'
    )
    password = serializers.CharField(
        trim_whitespace=True,
        label='Password'
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def validate_password(self, password):
        ''' проверки для пароля '''
        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError(
                "Password must contain at least one digit.",
                code="password_no_digit"
            )

        if not any(char.isupper() for char in password):
            raise serializers.ValidationError(
                "Password must contain at least one uppercase letter.",
                code="password_no_uppercase"
            )

        if not any(char.islower() for char in password):
            raise serializers.ValidationError(
                "Password must contain at least one lowercase letter.",
                code="password_no_lowercase"
            )
        if len(password) < 7:
            raise serializers.ValidationError(
                "Password must be at least 7 characters long.",
                code="password_length"
            )
        return password