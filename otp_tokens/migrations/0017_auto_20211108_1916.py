# Generated by Django 3.2.7 on 2021-11-08 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_tokens', '0016_auto_20211107_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardtoken',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 8, 20, 16, 56, 588937)),
        ),
        migrations.AlterField(
            model_name='cardverify',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 8, 19, 22, 56, 589583)),
        ),
    ]
