# Python imports
from datetime import datetime, timedelta
import pytz

# Django imports
from rest_framework.response import Response

# JWT imports
from rest_framework_simplejwt.tokens import RefreshToken

# import models (for typing)
from user.models.user import User


class JWTActions:
    ''' class for creating JWT and set cookies on response '''

    def __init__(
            self,
            response: Response = None,
            instance: User = None
        ) -> None:
        ''' attrs initialize
         
        Params:
        response: Response that we are going to return to user
        instance: obj of user Model, that we proccessing
        '''
        self.response = response
        self.instance = instance
        time_zone = pytz.UTC
        self.now = time_zone.localize(datetime.utcnow())

    def set_cookies_on_response(self):
        ''' set up cookies on response'''

        refresh_token = RefreshToken.for_user(self.instance)
        response_data = [
            {
                "cookie_key": "access_token",
                "cookie_value": str(refresh_token.access_token),
                "expires_at": self.now + timedelta(minutes=15),
                "secure_and_httponly": True,

            },
            {
                "cookie_key": "refresh_token",
                "cookie_value": str(refresh_token),
                "expires_at": self.now + timedelta(days=7),
                "secure_and_httponly": True,
            },
            {
                "cookie_key": "signed_in",
                "cookie_value": True,
                "expires_at": self.now + timedelta(minutes=15),
                "secure_and_httponly": True,
            }
        ]
        [
            self.response.set_cookie(
                obj["cookie_key"],
                obj["cookie_value"],
                expires=obj["expires_at"],
                secure=obj["secure_and_httponly"],
                httponly=obj["secure_and_httponly"],
                samesite="None",
                path="/api/v1/token/refresh/" if obj["cookie_key"] == "signed_in" else None
            )
            for obj in response_data
        ]
        return self.response
