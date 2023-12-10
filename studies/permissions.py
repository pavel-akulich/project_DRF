from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    message = 'Вы не являетесь модератором!'

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator').exists():
            return True
        return False


class IsNotModerator(BasePermission):
    message = 'Модераторы не могут создавать уроки или курсы!'

    def has_permission(self, request, view):
        if not request.user.groups.filter(name='moderator').exists():
            return True
        return False


class IsSuperUser(BasePermission):
    message = 'Вы не являетесь суперпользователем!'

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class IsOwner(BasePermission):
    message = 'Вы не являетесь владельцем!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False
