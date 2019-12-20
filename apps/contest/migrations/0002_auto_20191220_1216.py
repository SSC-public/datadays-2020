# Generated by Django 2.2.8 on 2019-12-20 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resources', '0001_initial'),
        ('participation', '0001_initial'),
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamtask',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='participation.Team'),
        ),
        migrations.AddField(
            model_name='task',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='resources.Document'),
        ),
        migrations.AddField(
            model_name='task',
            name='milestone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='contest.Milestone'),
        ),
    ]
