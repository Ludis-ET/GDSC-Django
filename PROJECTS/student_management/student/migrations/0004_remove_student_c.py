# Generated by Django 5.0 on 2024-01-10 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_c'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='c',
        ),
    ]
