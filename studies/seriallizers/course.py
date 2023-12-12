from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from studies.models import Course
from studies.seriallizers.lesson import LessonSerializer
from subscription.models import SubscriptionOnUpdate
from users.models import User


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели курса
    """
    # поле вывода количества уроков, относящихся к курсу
    lessons_count = serializers.IntegerField(source='lesson_set.all.count', required=False)
    # поле для вывода самих уроков(словарь с полями урока), относящихся к курсу
    lessons = LessonSerializer(source='lesson_set.all', many=True, required=False)

    subscription = serializers.SerializerMethodField(required=False)

    def get_subscription(self, obj):
        user = self.context['request'].user

        if user.is_authenticated:
            try:
                subscription = obj.subscriptiononupdate_set.get(user=user)
                return subscription.is_subscribed
            except SubscriptionOnUpdate.DoesNotExist:
                return False
        else:
            return False

    owner = SlugRelatedField(slug_field='first_name', queryset=User.objects.all(), required=False)

    class Meta:
        model = Course
        fields = ('pk', 'title', 'description', 'preview', 'lessons_count', 'lessons', 'owner', 'subscription',)
        read_only_fields = ('owner',)
