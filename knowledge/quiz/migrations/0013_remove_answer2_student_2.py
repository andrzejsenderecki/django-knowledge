# Generated by Django 2.0.1 on 2018-01-22 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_auto_20180122_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer2',
            name='student_2',
        ),
    ]
