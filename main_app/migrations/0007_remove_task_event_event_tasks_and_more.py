# Generated by Django 4.0.3 on 2022-04-08 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='tasks',
            field=models.ManyToManyField(blank=True, to='main_app.task'),
        ),
        migrations.AlterField(
            model_name='event',
            name='collaborators',
            field=models.ManyToManyField(blank=True, to='main_app.collaborator'),
        ),
    ]