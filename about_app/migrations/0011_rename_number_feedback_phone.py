# Generated by Django 3.2.13 on 2022-08-04 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0010_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='number',
            new_name='phone',
        ),
    ]
