# Django imports
from django.urls import path

# custom DRF classes imports
from user.views import UserActions

# JWT imports
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('create/', UserActions.as_view({'post': 'create_user'}), name='create_user'),
    path('login/', UserActions.as_view({'post': 'login_user'}), name='login_user'),
    path('/refresh_token/',
         TokenRefreshView.as_view(),
         name="refresh_token"),
]

#    path('telegram_create_user/', UserActions.as_view(
#        {'post': 'telegram_create_user'},
#        name='telegram_create_user'
#    )),