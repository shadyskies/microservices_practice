# Generated by Django 3.2.4 on 2021-07-16 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210716_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionmodel',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='quiz_images/'),
        ),
    ]