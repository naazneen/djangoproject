# Generated by Django 3.0.3 on 2020-02-15 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 15, 21, 29, 28, 683520)),
        ),
    ]
