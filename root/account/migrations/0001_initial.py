# Generated by Django 3.1.6 on 2021-02-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=256)),
                ('mob_phone', models.CharField(max_length=256)),
                ('avatar', models.FileField(upload_to='upload/')),
                ('address', models.TextField(max_length=1024)),
            ],
        ),
    ]
