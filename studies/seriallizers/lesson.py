from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from studies.models import Lesson
from users.models import User


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели урока
    """
    owner = SlugRelatedField(slug_field='first_name', queryset=User.objects.all())

    class Meta:
        model = Lesson
        fields = ('pk', 'title', 'description', 'preview', 'video_url', 'course', 'owner', )
