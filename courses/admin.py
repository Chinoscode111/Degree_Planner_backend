from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(User)
admin.site.register(CourseTaken)
# admin.site.register(Semester)
admin.site.register(CourseOffered)