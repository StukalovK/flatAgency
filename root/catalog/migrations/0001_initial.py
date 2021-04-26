# Generated by Django 3.1.6 on 2021-02-10 22:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=256)),
                ('content', models.TextField(max_length=1024)),
                ('address', models.CharField(max_length=256)),
                ('floor', models.IntegerField()),
                ('price', models.IntegerField()),
                ('publish', models.DateTimeField(default=datetime.datetime(2021, 2, 10, 22, 4, 11, 157009))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.district')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FileField(upload_to='flats/')),
                ('legend', models.CharField(max_length=256)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.offer')),
            ],
        ),
    ]
