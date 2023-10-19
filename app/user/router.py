from rest_framework.routers import DefaultRouter

from user.views import UserActions

router = DefaultRouter()
router.register(r'api/v1/user', UserActions, basename='user-actions')