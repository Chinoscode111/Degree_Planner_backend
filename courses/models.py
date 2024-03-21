# from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models

TITLE_CHOICES = [
    ('core', 'Core'),
    ('hasmed', 'Hasmed Elective'),
    ('minor', 'Minor'),
    ('honors', 'Honors'),
    ('dept_elective', 'Department Elective'),
]

# TODO: Check this...
GRADE_CHOICES = [
    ('AP', 10),
    ('AA', 10),
    ('AB', 9),
    ('BB', 8),
    ('BC', 7),
    ('CC', 6),
    ('DD', 5),
    ('FF', 0)   
]

STATUS = [
    ('completed', 'Completed'),
    ('inprogress', 'In Progress'),
    ('plan', 'Planned')
]

SEMESTER = [
    ('autumn', 'Autumn'),
    ('spring', 'Spring')
]

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.code} : {self.name}'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    password = models.CharField(max_length=10)
    rollnum = models.CharField(max_length=10, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    degree = models.CharField(max_length=100, default='B.Tech')
    def __str__(self):
        return self.rollnum

class Course(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    tag = models.CharField(max_length=20, choices=TITLE_CHOICES)
    credits = models.FloatField()
    semester = models.CharField(max_length=10, choices=SEMESTER)
    years = models.JSONField(default=list)
    def __str__(self):
        return self.title
    
class CourseOffered(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="courses_offered")
    prof = models.CharField(max_length=100)
    year = models.IntegerField()
    semester_type = models.CharField(max_length=10, choices=SEMESTER)   

class CourseTaken(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='courses_taken', to_field='rollnum', default=1)
    course = models.ForeignKey(CourseOffered, on_delete=models.CASCADE, related_name='courses_taken')
    # grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS, default='completed')

    def __str__(self):
        return f'{self.course.course.title} {self.course.course.code} {self.course.year}'