# Generated by Django 2.0.5 on 2018-09-23 10:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('EmpDetails', '0002_auto_20180923_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdetailsmodel',
            name='DOB',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 23, 10, 32, 45, 320931, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empdetailsmodel',
            name='Dateofjoining',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 23, 10, 32, 45, 321935, tzinfo=utc)),
        ),
    ]
