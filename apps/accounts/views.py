from rest_framework import viewsets

from apps.accounts.models import User
from apps.accounts.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
