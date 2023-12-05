from django.db import models

from studies.models import NULLABLE, Course, Lesson
from users.models import User


class Payment(models.Model):
    """
    Модель для платежа
    """
    PAYMENT_METHOD = [
        ('cash', 'наличные'),
        ('transfer to account', 'перевод на счет'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='урок', **NULLABLE)

    payment_amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.payment_date} - {self.payment_amount}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
