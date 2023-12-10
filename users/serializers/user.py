from rest_framework import serializers

from payments.models import Payment
from payments.serializers.payment import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя
    """
    user_payments = serializers.SerializerMethodField()

    def get_user_payments(self, obj):
        """
        Получает данные о платежах пользователей
        """
        payments = Payment.objects.filter(user=obj)
        payment_serializer = PaymentSerializer(payments, many=True)
        return payment_serializer.data

    def to_representation(self, instance):
        """
        Скрывает фамилию и платежи пользователя, если смотрим другой пользователь
        """
        data = super().to_representation(instance)
        requesting_user = self.context['request'].user

        if requesting_user.is_superuser or requesting_user == instance:
            return data

        data['last_name'] = f'Вам недоступна чужая фамилия'
        data['user_payments'] = f'Вам недоступны чужие платежи'
        return data

    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'phone', 'country', 'avatar', 'user_payments')
