# Generated by Django 3.1.6 on 2021-02-17 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 17, 20, 5, 27, 190425)),
        ),
    ]