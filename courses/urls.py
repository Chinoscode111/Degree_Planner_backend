# myapp/urls.py

from django.urls import path
from .views import CourseListCreateView
from .views import *

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('semester/', getCourseForSemester)
]
