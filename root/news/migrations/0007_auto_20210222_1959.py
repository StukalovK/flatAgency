# Generated by Django 3.1.6 on 2021-02-22 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20210217_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 22, 19, 59, 26, 121493)),
        ),
    ]
