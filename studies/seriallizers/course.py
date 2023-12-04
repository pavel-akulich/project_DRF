from rest_framework import serializers

from studies.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели курса
    """
    class Meta:
        model = Course
        fields = ('pk', 'title', 'description', 'preview',)
