# Generated by Django 4.1 on 2022-10-13 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_remove_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='Undefined', max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(default='Undefined', max_length=200),
        ),
    ]
