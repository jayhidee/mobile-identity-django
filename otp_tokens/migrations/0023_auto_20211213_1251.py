# Generated by Django 3.2.7 on 2021-12-13 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_tokens', '0022_auto_20211120_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardtoken',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 13, 51, 40, 363985)),
        ),
        migrations.AlterField(
            model_name='cardverify',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 12, 57, 40, 364629)),
        ),
    ]
