# Generated by Django 2.2.8 on 2020-01-31 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0003_auto_20200127_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirect',
            name='destination',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='redirect',
            name='source',
            field=models.CharField(max_length=512, unique=True),
        ),
    ]
