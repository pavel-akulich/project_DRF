from rest_framework import serializers

from studies.models import Course
from studies.seriallizers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели курса
    """
    # поле вывода количества уроков, относящихся к курсу
    lessons_count = serializers.IntegerField(source='lesson_set.all.count')
    # поле для вывода самих уроков(словарь с полями урока), относящихся к курсу
    lessons = LessonSerializer(source='lesson_set.all', many=True)

    class Meta:
        model = Course
        fields = ('pk', 'title', 'description', 'preview', 'lessons_count', 'lessons',)
