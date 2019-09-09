# Generated by Django 2.2.1 on 2019-08-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('minPrice', models.IntegerField()),
                ('maxPrice', models.IntegerField()),
                ('startDate', models.DateField()),
                ('starttime', models.TimeField()),
                ('endDate', models.DateField()),
                ('endtime', models.TimeField()),
                ('isPublished', models.BooleanField()),
                ('isDisabled', models.BooleanField()),
                ('isDeleted', models.BooleanField()),
                ('isActive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='EventSport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventId', models.CharField(max_length=100)),
                ('sportsId', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SportsMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=100)),
                ('sportsname', models.CharField(max_length=100)),
            ],
        ),
    ]
