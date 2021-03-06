from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings

from rest_framework.authentication import CSRFCheck
from rest_framework import exceptions


def enforce_csrf(request):
    check = CSRFCheck(request)
    check.process_request(request)
    reason = check.process_view(request, None, (), {})
    if reason:
        raise exceptions.PermissionDenied(f'CSRF Failed {reason}')


class CustomAuth(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        print(header)
        if header is None:
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
            print(raw_token)
        else:
            raw_token = self.get_raw_token(header)
            print(raw_token)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        print(validated_token)
        enforce_csrf(request)

        return self.get_user(validated_token), validated_token
