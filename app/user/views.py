# DRF imports
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.decorators import action

# import serializers
from user.serializers import CreateUserSerializer, LoginUserSerializer

# JWT imports
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

# import models
from user.models import User

# import custom foos
from user.hash import hashing


class UserActions(ViewSet):
    ''' class for creating and updating users '''
    http_method_names = ['post', 'update']
    lookup_field = 'id'

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
            validated_data = serializer.validated_data
            instance = serializer.save()
            instance.password = hashing(
                validated_data['password'],
                instance.id
            )
            instance.save()
            refresh_token = RefreshToken.for_user(instance)
            response_data = {
                "user": serializer.validated_data,
                'access_token': str(refresh_token.access_token),
                'refresh_token': str(refresh_token)
            }
            return Response(response_data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['post'], url_path="login_user")
    def login_user(self, request) -> Response:
        ''' login user '''
        # LoginUserSerializer
        serializer = self.get_serializer_class()
        print('zalupa')
        serializer = serializer(data=request.data)
        print('huy')
        if serializer.is_valid():
            validated_data = serializer.validated_data
            user = validated_data['password']['user']
            refresh_token = RefreshToken.for_user(user)
            response_data = {
                'access_token': str(refresh_token.access_token),
                'refresh_token': str(refresh_token)
            }
            return Response(response_data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
