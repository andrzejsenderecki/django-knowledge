# Generated by Django 2.0.1 on 2018-01-15 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_answer', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Answer2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_answer_1', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.CharField(max_length=100)),
                ('question_text', models.TextField()),
                ('answer_a', models.CharField(max_length=400)),
                ('answer_b', models.CharField(max_length=400)),
                ('answer_c', models.CharField(max_length=400)),
                ('answer_d', models.CharField(max_length=400)),
                ('answer_good', models.CharField(max_length=1)),
            ],
        ),
    ]
