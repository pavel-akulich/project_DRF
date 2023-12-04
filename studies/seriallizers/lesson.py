from rest_framework import serializers

from studies.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели урока
    """
    class Meta:
        model = Lesson
        fields = ('pk', 'title', 'description', 'preview', 'video_url', 'course')
