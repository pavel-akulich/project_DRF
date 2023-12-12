from rest_framework import status
from rest_framework.test import APITestCase

from studies.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
    """Тесты механизма CRUD уроков"""

    def setUp(self):
        self.user = User.objects.create(
            email='test@gmail.com',
            password='test'
        )
        self.user.is_superuser = True
        self.user.save()

        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """Тест для создания урока"""
        data = {
            'title': 'test for create',
            'description': 'test for create',
            'video_url': 'https://www.youtube.com/'
        }

        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'pk': 1,
                'title': 'test for create',
                'description': 'test for create',
                'preview': None,
                'video_url': 'https://www.youtube.com/',
                "course": None,
                "owner": ''
            }

        )

    def test_list_lesson(self):
        """Тест получения списка уроков"""
        lesson = Lesson.objects.create(
            title='list test',
            description='list test',
            video_url='https://www.youtube.com/'
        )

        response = self.client.get(
            '/lesson/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {'course': None,
                     'description': 'list test',
                     'owner': None,
                     'pk': lesson.pk,
                     'preview': None,
                     'title': 'list test',
                     'video_url': 'https://www.youtube.com/'}
                ]
            }
        )

    def test_detail_lesson(self):
        """Тест детального просмотра урока"""
        lesson = Lesson.objects.create(
            title='detail test',
            description='detail test',
            video_url='https://www.youtube.com/'
        )

        response = self.client.get(f'/lesson/detail/{lesson.pk}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': lesson.pk,
                'title': 'detail test',
                'description': 'detail test',
                'preview': None,
                'video_url': 'https://www.youtube.com/',
                'course': None,
                'owner': None
            }
        )

    def test_update_lesson(self):
        """Тест для обновления урока"""
        lesson = Lesson.objects.create(
            title='test for update',
            description='test for update',
            video_url='https://www.youtube.com/'
        )

        updated_data = {
            'title': 'updated title',
            'description': 'updated description',
            'video_url': 'https://www.youtube.com/'
        }

        response = self.client.put(
            f'/lesson/update/{lesson.pk}/',
            data=updated_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': lesson.pk,
                'title': 'updated title',
                'description': 'updated description',
                'preview': None,
                'video_url': 'https://www.youtube.com/',
                'course': None,
                'owner': None
            }
        )

    def test_delete_lesson(self):
        """Тест для удаления урока"""
        lesson = Lesson.objects.create(
            title='test for delete',
            description='test for delete',
            video_url='https://www.youtube.com/'
        )

        response = self.client.delete(
            f'/lesson/delete/{lesson.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
