# Generated by Django 3.2.4 on 2021-07-16 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_resultmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizmodel',
            name='data_submitted',
        ),
    ]