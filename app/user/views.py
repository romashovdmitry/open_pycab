# DRF imports
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.decorators import action

# import serializers
from user.serializers import UserSerializer

# JWT imports
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

# import custom foos
from user.hash import hashing


class UserActions(ViewSet):
    ''' class for creating and updating users '''
    http_method_names = ['post', 'update']
    serializer_class = UserSerializer
    lookup_field = 'id'
    
    @action(detail=False, methods=['post'], url_path="registrate_user")
    def registrate_user(self, request) -> Response:
        ''' creating new user '''
        serializer = self.serializer_class(data=request.data)
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
        return Response(status=HTTP_200_OK)
