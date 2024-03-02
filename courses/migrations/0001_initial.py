# Generated by Django 5.0.2 on 2024-03-02 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=20)),
                ('tag', models.CharField(choices=[('core', 'Core'), ('hasmed', 'Hasmed Elective'), ('minor', 'Minor'), ('honors', 'Honors'), ('dept_elective', 'Department Elective')], max_length=20)),
                ('semester', models.IntegerField()),
                ('credits', models.FloatField()),
            ],
        ),
    ]