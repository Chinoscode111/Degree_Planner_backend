# Generated by Django 5.0.2 on 2024-03-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('fall', 'Fall'), ('spring', 'Spring')], max_length=20),
        ),
    ]