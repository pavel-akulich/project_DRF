from rest_framework import generics, serializers

from studies.permissions import IsSuperUser
from subscription.models import SubscriptionOnUpdate
from subscription.serializers.subscription import SubscriptionOnUpdateSerializer
from subscription.permissions import IsOwner


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания подписки на обновления курса
    """
    serializer_class = SubscriptionOnUpdateSerializer

    def perform_create(self, serializer):
        """ Проверяет, существует ли подписка данного пользователя на обновления курса"""
        user = self.request.user
        course = serializer.validated_data['course']

        if not SubscriptionOnUpdate.objects.filter(user=user, course=course).exists():
            serializer.save(user=user)
        else:
            raise serializers.ValidationError("Вы уже подписаны на обновления этого курса")


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    """
    Представление для удаления объекта
    """
    queryset = SubscriptionOnUpdate.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class SubscriptionListAPIView(generics.ListAPIView):
    """
    Представление для списка подписок
    """
    queryset = SubscriptionOnUpdate.objects.all()
    serializer_class = SubscriptionOnUpdateSerializer
    permission_classes = [IsSuperUser]
