

from django.urls import path
from .views import *

# URL Path: /api/___

urlpatterns = [
    path('semester/', getCourseForSemester), # Requires rollnum
    path('courses/', getCourses), 
    path('userCourses/', getUserCourses), # Requires rollnum
    path('progress/', getProgress), # Requires rollnum
    path('register/', register_view),
    path('login/', login_view),
    path('course/', addCourse)
]