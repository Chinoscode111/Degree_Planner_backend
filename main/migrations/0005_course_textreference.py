# Generated by Django 5.0.2 on 2024-02-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_course_code_alter_department_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='textreference',
            field=models.CharField(default='NA', max_length=1000),
        ),
    ]
