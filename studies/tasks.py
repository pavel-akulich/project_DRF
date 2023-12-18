from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def update_material_mail(email):
    """Задача для рассылки сообщения при обновлении курса"""

    send_mail(
        subject='Обновление материалов курса',
        message='У нас произошли обновления в материалах курса, проверьте что нового',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
