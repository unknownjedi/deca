# Generated by Django 2.1.4 on 2019-09-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_selection_templates'),
    ]

    operations = [
        migrations.AddField(
            model_name='templates',
            name='submit',
            field=models.TextField(default=''),
        ),
    ]