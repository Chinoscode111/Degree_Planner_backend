from django.shortcuts import render
from numpy import roll
from rest_framework import generics
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

@api_view(['GET'])
@login_required
def getCourseForSemester(request):
    rollnum = request.user.student.rollnum
    student = Student.objects.get(rollnum=rollnum.lower())
    data = {}
    for course in student.courses_taken.all():
        if course.course.semester_type not in data:
            data[course.course.semester_type] = []
        data[course.course.semester_type].append({
            'title': course.course.course.title,
            'code': course.course.course.code,
            'year': course.course.year
        })
    return Response(data)



# Course API
@api_view(['GET'])
def getCourses(request):
    courses = Course.objects.all()
    data = list()
    for course in courses:
        data.append({
            'code': course.code,
            'title': course.title,
            'semester':course.semester,
            'credits': course.credits,
            'tag': course.tag,
            'year': course.years
        })
        print(course)
    return Response(data)


@api_view(['POST'])
def addCourse(request):
    try:
        student_rollnum = request.data.get('student_rollnum')
        course_offered_code = request.data.get('course_offered_code')
        status = request.data.get('status')
        study_year = request.data.get('study_year') 


        student = Student.objects.get(rollnum=student_rollnum)
        course_offered = CourseOffered.objects.get(course__code=course_offered_code)

        course_taken = CourseTaken.objects.create(
            student=student,
            course=course_offered,
            status=status, 
            study_year=study_year
        )

        return JsonResponse({'message': 'Course added successfully.'}, status=201)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found.'}, status=404)
    except CourseOffered.DoesNotExist:
        return JsonResponse({'error': 'Course not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@api_view(['GET'])
@login_required
def getUserCourses(request):
    rollnum = request.user.student.rollnum
    student = Student.objects.get(rollnum=rollnum.lower())
    data = {}
    for course_taken in student.courses_taken.all():
        year = course_taken.course.year
        semester = 'Autumn' if course_taken.course.semester_type == 1 else 'Spring'
        if year not in data:
            data[year] = {}
        if semester not in data[year]:
            data[year][semester] = {}
        data[year][semester][course_taken.course.code] = {
            'title': course_taken.course.title,
            'code': course_taken.course.code,
            'semester': semester,
            'credits': course_taken.course.credits,
            'tag': course_taken.course.tag,
            'status': course_taken.status
        }
    return Response(data)


@api_view(['GET'])
@login_required
def getProgress(request):
    rollnum = request.user.student.rollnum
    student = Student.objects.get(rollnum=rollnum.lower())
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

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')
        password = request.POST.get('password')
        print(roll_number, password)
        print(User.objects.all().get(username=roll_number).password == password)
        user = authenticate(request, username=roll_number, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'})
    
@csrf_exempt
def register_view(request):
    if request.method == 'POST':

        roll_number = request.POST.get('roll_number')
        password = request.POST.get('password')
        department = request.POST.get('department')
        degree = request.POST.get('degree')
        # Rest of the code...
        if User.objects.filter(username=roll_number).exists():
            return JsonResponse({'status': 'error', 'message': 'User already exists'})

        profile = User.objects.create_user(username=roll_number, password=password)
        profile.student = Student(user=profile, password=password, rollnum=roll_number, department=Department.objects.get(code=department), degree=degree)
        profile.save()
        profile.student.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'})