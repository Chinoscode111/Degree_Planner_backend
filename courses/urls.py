# myapp/urls.py

from django.urls import path
from .views import CourseListCreateView
from .views import *

# URL Path: /api/___

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('semester/', getCourseForSemester), # Requires rollnum
    path('course/', getCourses), 
    path('userCourses/', getUserCourses), # Requires rollnum
    path('progress/', getProgress), # Requires rollnum
]