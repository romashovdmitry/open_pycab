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
    
    def validate_username(self, username):
        ''' проверка уникальности username '''
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                "Username already exists",
                code='username_exists'
            )
        return username

    def validate_email(self, email):
        ''' проверка уникальности username '''
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "email already exists",
                code='email_exists'
            )
        return email