# Generated by Django 4.1 on 2022-10-13 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_task_isfinished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='title',
        ),
    ]
