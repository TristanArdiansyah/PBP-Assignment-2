# Generated by Django 4.1 on 2022-10-13 02:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0009_alter_task_description_alter_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
