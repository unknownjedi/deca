# Generated by Django 2.1.4 on 2019-09-27 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190927_1437'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='eventsport',
            name='tf',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sportsmaster',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='sportsmaster',
            name='group',
            field=models.CharField(default='', max_length=200),
        ),
    ]
