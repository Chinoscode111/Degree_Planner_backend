# myapp/models.py

from django.db import models

class Course(models.Model):
    TITLE_CHOICES = [
        ('core', 'Core'),
        ('hasmed', 'Hasmed Elective'),
        ('minor', 'Minor'),
        ('honors', 'Honors'),
        ('dept_elective', 'Department Elective'),
    ]

    title = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    tag = models.CharField(max_length=20, choices=TITLE_CHOICES)
    semester = models.IntegerField()
    credits = models.FloatField()

    def __str__(self):
        return self.title

