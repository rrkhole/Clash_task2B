# Generated by Django 3.0.8 on 2020-08-11 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0003_profile_uname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='uname',
        ),
    ]
