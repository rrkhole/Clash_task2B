# Generated by Django 3.0.8 on 2020-08-11 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0002_auto_20200811_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='uname',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
