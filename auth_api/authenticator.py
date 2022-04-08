from rest_framework import authentication, exceptions

from auth_api.models import CustomUser


class CustomAuthenticate(authentication.BaseAuthentication):
    """
    Made only for testing purposes. Wasn't quite sure of the authentication and permission requirements.
    After all it's not used.
    Made to authenticate the user with email, which is in the request headers.
    """
    def authenticate(self, request):
        email = request.headers.get('X_Email')
        if not email:
            return None

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed("You have to register, for access this page")

        return (user, None)
