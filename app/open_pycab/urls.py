# Dajango imports
from django.contrib import admin
from django.urls import path, include


# from rest_framework.throttling import UserRateThrottle
#class CustomTokenObtainPairView(TokenObtainPairView):
#    ''' to get both JWT tokens with limitation '''
#    throttle_classes = [UserRateThrottle]


urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # JWT
    # user create, login, logout, 
    path('api/v1/user/', include("users.urls")),
    path('api/v1/telegram/', include("users.urls")),
    # cards create, update, delete
    path('api/v1/text/', include("cards.urls"))
]

