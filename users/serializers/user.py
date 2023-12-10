from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя
    """

    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'phone', 'country', 'avatar',)
