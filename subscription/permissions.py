from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = 'Вы не являетесь владельцем этой подписки!'

    def has_object_permission(self, request, view, obj):
        """Проверяет, является ли текущий пользователь владельцем подписки"""
        return obj.user == request.user
