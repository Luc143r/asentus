# Generated by Django 3.2.13 on 2022-08-04 22:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0011_rename_number_feedback_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
