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

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.code} : {self.name}'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    rollnum = models.CharField(max_length=10, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    semester = models.IntegerField(default=1)
    groups = models.ManyToManyField(Group, related_name="custom_user_set", default=1)
    degree = models.CharField(max_length=100, default='B.Tech')
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_set",default=1)
    def __str__(self):
        return self.username

class Course(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    tag = models.CharField(max_length=20, choices=TITLE_CHOICES)
    credits = models.FloatField()
    semester = models.IntegerField(default=1)
    years = models.JSONField(default=list)
    def __str__(self):
        return self.title
    
class CourseOffered(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="courses_offered")
    prof = models.CharField(max_length=100)
    year = models.IntegerField()
    semester_type = models.IntegerField(default=1)

class CourseTaken(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='courses_taken', to_field='rollnum', default=1)
    course = models.ForeignKey(CourseOffered, on_delete=models.CASCADE, related_name='courses_taken')
    # grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    study_year = models.IntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS, default='completed')

    def __str__(self):
        return f'{self.course.course.title} {self.course.course.code} {self.course.year}'