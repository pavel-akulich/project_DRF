from django.contrib import admin

from studies.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'preview', 'description', 'owner', 'updated_at',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'preview', 'video_url', 'course', 'owner',)
