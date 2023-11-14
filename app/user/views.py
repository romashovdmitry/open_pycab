# Python imports
from sys import stdout

# DRF imports
from rest_framework.viewsets import ViewSet
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

# import serializers
from user.serializers import CreateUserSerializer, LoginUserSerializer

# import models
from user.models import User

# import custom foos, classes
from user.hash import hashing
from user.services import JWTActions

# import constants
from open_pycab.settings import HTTP_HEADERS


class UserActions(ViewSet):
    ''' class for creating and updating users '''
    http_method_names = ['post', 'update']
    lookup_field = 'id'
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        ''' define serializer for class '''
        if self.action == 'create_user':
            return CreateUserSerializer
        elif self.action == 'login_user':
            return LoginUserSerializer

    @action(detail=False, methods=['post'], url_path="create_user")
    def create_user(self, request) -> Response:
        ''' creating new user '''
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)

        if serializer.is_valid():
            stdout.write("COME HERE")
            validated_data = serializer.validated_data
            instance = serializer.save()
            instance.password = hashing(
                validated_data['password'],
                instance.id
            )
            instance.save()
            return_response = Response(
                status=HTTP_201_CREATED,
                headers=HTTP_HEADERS,
                data={
                    "username": serializer.validated_data["username"]
                }
            )
            return JWTActions(
                response=return_response,
                instance=instance                
            ).set_cookies_on_response()

        else:

            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['post'], url_path="login_user")
    def login_user(self, request) -> Response:
        ''' login user '''
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        cookies_str = "\n".join([f"{key}: {value}" for key, value in request.COOKIES.items()])
        # строка выше забирает куки из отправленного запрос. 
        stdout.write(cookies_str)
        # печатает их в консоль.         

        if serializer.is_valid():
            stdout.write(cookies_str)
            validated_data = serializer.validated_data
            user = validated_data['password']['user']
            return_response = HttpResponse(
                status=HTTP_200_OK,
                headers=HTTP_HEADERS,
                data={
                    "username": serializer.validated_data["password"]["user"].username
                }
            )
            return JWTActions(
                response=return_response,
                instance=user
            ).set_cookies_on_response()

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path="generate_telegram_password")
    def generate_telegram_password(self, request) -> Response:
        ''' registrate telegram id of user '''
        user = User.objects.get(request.data["user_id"])
        user.set_telegram_password()
        return Response(
            data={"telegram_password": user.telegram_password},
            status=HTTP_201_CREATED
        )

    

'''
    @action(detail=False, methods=['post'], url_path="create_user")
    def check_telegram_password(self, request) -> Response:
        user = User.objects.get(request.data["user_id"])
        if user.telegram_password == request.data["telegram_password"]
        return Response(
            data={"telegram_password": user.telegram_password},
            status=HTTP_201_CREATED
        )
'''