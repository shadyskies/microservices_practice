# Generated by Django 3.2.4 on 2021-07-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionmodel',
            name='option1',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='option2',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='option3',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='option4',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
