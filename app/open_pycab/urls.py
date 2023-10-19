# Dajango imports
from django.contrib import admin
from django.urls import path

# import routing
from user.router import router

# JWT imports
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.throttling import UserRateThrottle


class CustomTokenObtainPairView(TokenObtainPairView):
    ''' to get both JWT tokens with limitation '''
    throttle_classes = [UserRateThrottle]


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/token/', CustomTokenObtainPairView.as_view()),
    path('api/v1/token/refresh/', TokenRefreshView.as_view()),
]

urlpatterns += router.urls
