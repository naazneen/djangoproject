# Generated by Django 3.0.3 on 2020-03-05 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200305_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 5, 20, 56, 59, 6298)),
        ),
    ]
