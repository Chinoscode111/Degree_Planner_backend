# Generated by Django 5.0.2 on 2024-03-11 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_rename_semester_type_course_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursetaken',
            name='semester_type',
        ),
        migrations.AddField(
            model_name='courseoffered',
            name='semester_type',
            field=models.IntegerField(default=1),
        ),
    ]