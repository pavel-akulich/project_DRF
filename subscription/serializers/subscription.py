from rest_framework import serializers

from subscription.models import SubscriptionOnUpdate


class SubscriptionOnUpdateSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели подписки на обновления курса """

    class Meta:
        model = SubscriptionOnUpdate
        fields = ('pk', 'user', 'course', 'is_subscribed')
        read_only_fields = ('user',)
