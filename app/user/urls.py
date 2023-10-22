# Django imports
from django.urls import path

# custom DRF classes imports
from user.views import UserActions


urlpatterns = [
    path('registrate_user/', UserActions.as_view({'post': 'registrate_user'}), name='registrate_user'),
    path('login_user/', UserActions.as_view({'post': 'login_user'}), name='login_user')
]