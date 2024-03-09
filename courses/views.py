from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

@api_view(['GET'])
def getCourseForSemester(request):
    rollnum = request.GET['rollnum']    
    print(rollnum)
    student = User.objects.get(rollnum=rollnum.lower())
    print(student)
    # semester = request.GET['semester']
    courses = student.semesters.get(semester_type=student).courses.all()
    print(courses)
    # data = {
    #     courses
    # }
    # return Response(data)
    data = dict()
    for course in student.courses_taken.all():
        data['title'] = course.course.title
        data['code'] = course.course.code
    return Response(data)
