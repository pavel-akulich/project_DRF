import random
from decimal import Decimal

from django.core.management import BaseCommand
from django.utils import timezone

from payments.models import Payment
from studies.models import Course, Lesson
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Команда для записи рандомного платежей в модель
        """
        users = User.objects.all()
        courses = Course.objects.all()
        lessons = Lesson.objects.all()

        payment = Payment(
            user=random.choice(users) if users else None,
            payment_date=timezone.now(),
            course=random.choice(courses) if courses else None,
            lesson=random.choice(lessons) if lessons else None,
            payment_amount=Decimal(random.randrange(100, 50000)),
            payment_method=random.choice(['cash', 'transfer to account'])
        )

        payment.save()
