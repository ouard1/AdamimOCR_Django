# serializers.py

from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username')
