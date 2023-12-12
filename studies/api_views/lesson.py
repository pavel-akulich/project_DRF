from rest_framework import generics

from studies.models import Lesson
from studies.paginators import LessonPaginator
from studies.permissions import IsOwner, IsModerator, IsNotModerator, IsSuperUser
from studies.seriallizers.lesson import LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания объекта
    """
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()

    permission_classes = [IsNotModerator]


class LessonListAPIView(generics.ListAPIView):
    """
    Представление для просмотра списка объектов
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonPaginator

    def get_queryset(self):
        """
        Переопределение queryset для уроков
        """
        # Если пользователь - модератор или суперпользователь, то возвращаем все уроки
        if self.request.user.groups.filter(name='moderator').exists() or self.request.user.is_superuser:
            return Lesson.objects.all()

        # Если пользователь - не модератор, тогда возвращаем уроки принадлежащие пользователю
        return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Представление для детального просмотра объекта
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsModerator | IsSuperUser]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Представление для обновления объекта
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsModerator | IsSuperUser]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Представление для удаления объекта
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsSuperUser]
