from django.conf import settings
from django.db import models

from studies.models import Course


class SubscriptionOnUpdate(models.Model):
    """Подписка на обновления курса"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    is_subscribed = models.BooleanField(default=True, verbose_name='признак подписки')

    def __str__(self):
        return f'{self.user} - {self.course} - {self.is_subscribed}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
