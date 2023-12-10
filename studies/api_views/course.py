from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from studies.models import Course
from studies.permissions import IsNotModerator, IsOwner, IsModerator, IsSuperUser
from studies.seriallizers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    Представление CRUD для модели курсов
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        """
        Права доступа для курсов
        """
        if self.action == 'create':
            permission_classes = [IsNotModerator]
        elif self.action == 'retrieve':
            permission_classes = [IsOwner | IsModerator | IsSuperUser]
        elif self.action == 'update':
            permission_classes = [IsOwner | IsModerator | IsSuperUser]
        elif self.action == 'destroy':
            permission_classes = [IsOwner | IsSuperUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """
        Переопределение queryset для курсов
        """
        # Если пользователь - модератор или суперпользователь, то возвращаем все курсы
        if self.request.user.groups.filter(name='moderator').exists() or self.request.user.is_superuser:
            return Course.objects.all()

        # Если пользователь - не модератор, тогда возвращаем курсы, принадлежащие пользователю
        return Course.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Запись владельца при создании курса
        """
        serializer.save(owner=self.request.user)
