from rest_framework import serializers


def validator_urls(value):
    """Валидатор для ссылок на уроки"""
    if 'youtube.com' not in value.lower():
        raise serializers.ValidationError(f'нельзя использовать ссылку {value}, допускаются ссылки на YouTube')
