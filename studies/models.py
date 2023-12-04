from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """
    Модель для курса
    """
    title = models.CharField(max_length=150, verbose_name='название курса')
    preview = models.ImageField(upload_to='course_previews/', verbose_name='превью курса', **NULLABLE)
    description = models.TextField(verbose_name='описание курса')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    """
    Модель для уроков
    """
    title = models.CharField(max_length=150, verbose_name='название урока')
    description = models.TextField(verbose_name='описание урока')
    preview = models.ImageField(upload_to='lesson_previews/', verbose_name='превью урока', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')

    def __str__(self):
        return f'{self.title} - {self.video_url}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
