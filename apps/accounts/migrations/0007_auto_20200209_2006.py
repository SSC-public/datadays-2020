# Generated by Django 2.2.9 on 2020-02-09 20:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200207_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '09001234567'. Up to 15 digits allowed.", regex='^0?\\d{11}$')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='student_id',
            field=models.IntegerField(null=True),
        ),
    ]
