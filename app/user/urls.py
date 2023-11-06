# Django imports
from django.urls import path

# custom DRF classes imports
from user.views import UserActions


urlpatterns = [
    path('create_user/', UserActions.as_view({'post': 'create_user'}), name='create_user'),
    path('login_user/', UserActions.as_view({'post': 'login_user'}), name='login_user'),
    path('telegram_create_user/', UserActions.as_view(
        {'post': 'telegram_create_user'},
        name='telegram_create_user'
    )),
]