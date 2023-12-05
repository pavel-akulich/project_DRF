from rest_framework import serializers

from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели платежа
    """

    class Meta:
        model = Payment
        fields = ('pk', 'user', 'payment_date', 'course', 'lesson', 'payment_amount', 'payment_method',)
