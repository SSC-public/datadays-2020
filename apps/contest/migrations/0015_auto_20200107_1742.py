# Generated by Django 2.2.8 on 2020-01-07 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0014_auto_20200106_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsubmission',
            name='file_answer',
            field=models.BooleanField(default=False),
        ),
    ]
