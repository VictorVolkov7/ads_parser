from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView as BaseTokenObtainPairView, \
    TokenRefreshView as BaseTokenRefreshView

from users.serializers import UserSerializer


@extend_schema(
    summary="API endpoint for user registration."
)
class UserCreateAPIView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@extend_schema(
    summary="Used to request a pair of tokens (access and refresh).",
)
class TokenObtainPairView(BaseTokenObtainPairView):
    """
    A placeholder for a class to supplement documentation.
    """
    pass


@extend_schema(
    summary="Used to refresh an access token when it expires.",
)
class TokenRefreshView(BaseTokenRefreshView):
    """
    A placeholder for a class to supplement documentation.
    """
    pass
