# Dajango imports
from django.contrib import admin
from django.urls import path, include

# JWT imports
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.throttling import UserRateThrottle


class CustomTokenObtainPairView(TokenObtainPairView):
    ''' to get both JWT tokens with limitation '''
    throttle_classes = [UserRateThrottle]


urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # JWT
    path('api/v1/token/', CustomTokenObtainPairView.as_view()),
    path('api/v1/token/refresh/', TokenRefreshView.as_view()),
    # user create, login, logout
    path('api/v1/user/', include("user.urls")),
    # cards create, update, delete
    path('api/v1/text/', include("cards.urls"))
]
