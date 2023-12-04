from rest_framework import viewsets

from studies.models import Course
from studies.seriallizers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
