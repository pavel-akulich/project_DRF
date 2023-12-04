# Generated by Django 5.0 on 2023-12-04 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название курса')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='course_previews/', verbose_name='превью курса')),
                ('description', models.TextField(verbose_name='описание курса')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название урока')),
                ('description', models.TextField(verbose_name='описание урока')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='lesson_previews/', verbose_name='превью урока')),
                ('video_url', models.URLField(verbose_name='ссылка на видео')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studies.course', verbose_name='курс')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]
