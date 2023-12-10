from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from payments.models import Payment
from users.models import User


class PaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели платежа
    """
    user = SlugRelatedField(slug_field='first_name', queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = ('pk', 'user', 'payment_date', 'course', 'lesson', 'payment_amount', 'payment_method',)
