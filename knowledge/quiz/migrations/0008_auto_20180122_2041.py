# Generated by Django 2.0.1 on 2018-01-22 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20180122_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer1',
            name='student',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
