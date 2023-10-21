# DRF imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

# import serializers
from user.serializers import UserSerializer

# JWT imports
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

# import custom foos
from user.hash import hashing


class UserActions(ModelViewSet):
    ''' class for creating and updating users '''
    http_method_names = ['post', 'update']
    serializer_class = UserSerializer
    lookup_field = 'id'
    
    def create(self, request, *args, **kwargs) -> Response:
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