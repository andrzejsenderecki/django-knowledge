# Generated by Django 2.0.1 on 2018-01-22 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20180122_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer1',
            old_name='author',
            new_name='student',
        ),
    ]
