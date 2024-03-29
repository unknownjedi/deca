# Generated by Django 2.2.1 on 2019-09-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_eventmaster_eventsport_sportsmaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sportbtn', models.BooleanField()),
                ('location', models.BooleanField()),
                ('userid', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeof', models.CharField(max_length=20)),
                ('sportbtn', models.TextField()),
                ('location', models.TextField()),
                ('userid', models.TextField()),
            ],
        ),
    ]
