

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=20)),
                ('tag', models.CharField(choices=[('core', 'Core'), ('hasmed', 'Hasmed Elective'), ('minor', 'Minor'), ('honors', 'Honors'), ('dept_elective', 'Department Elective')], max_length=20)),
                ('credits', models.FloatField()),
                ('semester', models.IntegerField(default=1)),
                ('years', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='CourseOffered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('semester_type', models.IntegerField(default=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_offered', to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('rollnum', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('semester', models.IntegerField(default=1)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='courses.department')),
                ('groups', models.ManyToManyField(default=1, related_name='custom_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(default=1, related_name='custom_user_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CourseTaken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_year', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('inprogress', 'In Progress'), ('plan', 'Planned')], default='completed', max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_taken', to='courses.courseoffered')),
                ('student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='courses_taken', to='courses.user')),
            ],
        ),
    ]
