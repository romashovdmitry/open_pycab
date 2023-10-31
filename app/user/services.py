# Django imports
from rest_framework.response import Response

# JWT imports
from rest_framework_simplejwt.tokens import RefreshToken

# import models (for typing)
from user.models.user import User


class JWT_actions:
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

    def set_cookies_on_response(self):
        ''' set up cookies on response'''
        refresh_token = RefreshToken.for_user(self.instance)
        response_data = [
            {
                "cookie_key": "access_token",
                "cookie_value": str(refresh_token.access_token)
            },
            {
                "cookie_key":"refresh_token",
                "cookie_value": str(refresh_token)
            }
        ]
        [
                self.response.set_cookie(
                    obj["cookie_key"],
                    obj["cookie_value"],
                    httponly=True,
                    secure=True
                )
                for obj in response_data
        ]
        return self.response