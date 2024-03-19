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
    courses = student.courses_taken.all()
    print(courses)
    # data = {
    #     courses
    # }
    # return Response(data)
    data = dict()
    for course in student.courses_taken.all():
        data = dict()
        if data.keys().__contains__(course.semester_type):
            data[course.semester_type].append(course)
    return Response(data)


# Course API
@api_view(['GET'])
def getCourses(request):
    courses = Course.objects.all()
    data = dict()
    for course in courses:
        data[course.code] = {
            'code': course.code,
            'title': course.title,
            'semester': 'Autumn' if course.semester == 1 else 'Spring',
            'credits': course.credits,
            'tag': course.tag,
            'year': list(course.years)
        }
        print(course)
    return Response(data)

@api_view(['GET'])
def getUserCourses(request):
    rollnum = request.GET['rollnum']
    student = User.objects.get(rollnum=rollnum.lower())
    courses = student.courses_taken.all()
    data = dict()
    for course in courses:
        data[course.course.year] = {}
        data[course.course.year]['Autumn' if course.course.semester_type == 1 else 'Spring'] = {}

    for course in courses:
        data[course.course.year]['Autumn' if course.course.semester_type == 1 else 'Spring'][course.course.course.code] = {
            'code': course.course.course.code,
            'title': course.course.course.title,
            'semester': 'Autumn' if course.course.semester_type == 1 else 'Spring',
            'credits': course.course.course.credits,
            'tag': course.course.course.tag,
            'status': course.status
        }
    return Response(data)

@api_view(['GET'])
def getProgress(request):
    rollnum = request.GET['rollnum']
    student = User.objects.get(rollnum=rollnum.lower())
    courses = student.courses_taken.all()
    data = {
        'total_credits': 0,
        'core_credits': 0,
        'elective_credits': 0,
        'minor_credits': 0,
        'honors_credits': 0,
        'hasmed_credits': 0
    }
    for course in courses:
        data['total_credits'] += course.course.course.credits
        if course.course.course.tag == 'core':
            data['core_credits'] += course.course.course.credits
        elif course.course.course.tag == 'dept_elective':
            data['elective_credits'] += course.course.course.credits
        elif course.course.course.tag == 'minor':
            data['minor_credits'] += course.course.course.credits
        elif course.course.course.tag == 'honors':
            data['honors_credits'] += course.course.course.credits
        elif course.course.course.tag == 'hasmed':
            data['hasmed_credits'] += course.course.course.credits
    return Response(data)
    