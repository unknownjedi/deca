# Generated by Django 2.1.4 on 2019-09-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190904_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templates',
            name='url',
        ),
        migrations.AddField(
            model_name='selection',
            name='url',
            field=models.TextField(default=''),
        ),
    ]
