# Generated by Django 3.2.7 on 2021-11-07 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_tokens', '0014_auto_20211107_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardtoken',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 7, 20, 46, 23, 473278)),
        ),
        migrations.AlterField(
            model_name='cardverify',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 7, 19, 52, 23, 473938)),
        ),
    ]
