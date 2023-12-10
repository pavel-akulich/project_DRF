from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = 'Вы не являетесь владельцем этого профиля!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False
