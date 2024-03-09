
from django.contrib.auth.models import AbstractUser, Group, Permission
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

COLLEGE_YEAR = [
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Third'),
    ('4', 'Fourth'),
    ('5', 'Fifth'),
    ('6', 'Sixth'),
    ('7', 'Seventh'),
    ('8', 'Eighth'),
    ('9', 'Ninth'),
    ('10', 'Tenth')
]

SEMESTER_TYPE_CHOICES = [
    ('1', 'Autumn'),
    ('2', 'Spring'),
]

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.code} : {self.name}'

class User(AbstractUser):
    rollnum = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    semester = models.CharField(max_length=2, choices=COLLEGE_YEAR)
    groups = models.ManyToManyField(Group, related_name="custom_user_set")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_set")
    def __str__(self):
        return self.username

class Course(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    tag = models.CharField(max_length=20, choices=TITLE_CHOICES)
    credits = models.FloatField()

    def __str__(self):
        return self.title
    
class CourseOffered(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="courses_offered")
    prof = models.CharField(max_length=100)
    year = models.IntegerField()
    semester_type = models.CharField(max_length=1, choices=SEMESTER_TYPE_CHOICES    )   

class CourseTaken(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_taken')
    course = models.ForeignKey(CourseOffered, on_delete=models.CASCADE, related_name='courses_taken')
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    semester_type = models.CharField(max_length=1, choices=SEMESTER_TYPE_CHOICES)
    study_year = models.CharField(max_length=2, choices=COLLEGE_YEAR)

    def __str__(self):
        return f'{self.course.course.title} {self.course.course.code} {self.course.year}'