# Generated by Django 2.1.4 on 2019-09-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20190927_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilitymaster',
            name='maxPrice',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='facilitymaster',
            name='minPrice',
            field=models.FloatField(default=0, null=True),
        ),
    ]
