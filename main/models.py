from django.db import models

# Create your models here.

SEMESTER_CHOICES = [
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

class Course(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    description = models.TextField()
    credit = models.IntegerField()
    prerequisite = models.ManyToManyField('self', blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    textreference = models.CharField(max_length=1000, default='NA')
    semester_type = models.CharField(max_length=1, choices=SEMESTER_TYPE_CHOICES)

    def __str__(self):
        return f'{self.code} : {self.name}'
    
class User(models.Model):
    name = models.CharField(max_length=100)
    rollnum = models.CharField(max_length=10)
    email = models.EmailField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES)

    def __str__(self):          
        return f'{self.name}'
