from rest_framework import status
from rest_framework.test import APITestCase

from studies.models import Course
from subscription.models import SubscriptionOnUpdate
from users.models import User


class LessonTestCase(APITestCase):
    """Тесты функционала работы подписки на обновления курса"""

    def setUp(self):
        self.user = User.objects.create(
            email='test@gmail.com',
            password='test'
        )
        self.user.is_superuser = True
        self.user.save()

        self.client.force_authenticate(user=self.user)

    def test_create_subscription(self):
        """Тест для создания подписки на курс"""

        course = Course.objects.create(
            title='test_subscription',
            description='test_subscription'
        )

        data = {
            'course': 1
        }

        response = self.client.post(
            '/subscription/subscription/activate/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                "pk": 1,
                "user": self.user.pk,
                "course": course.pk,
                "is_subscribed": False
            }
        )

    def test_delete_subscription(self):
        """Тест для удаления подписки на обновления курса"""

        course = Course.objects.create(
            title='test delete',
            description='test delete'
        )

        subscription = SubscriptionOnUpdate.objects.create(
            user=self.user,
            course=course,
            is_subscribed=True
        )

        response = self.client.delete(
            f'/subscription/subscription/deactivate/{subscription.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
