# Generated by Django 3.2.7 on 2022-01-18 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_tokens', '0027_auto_20220113_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardtoken',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 18, 14, 38, 12, 216476)),
        ),
        migrations.AlterField(
            model_name='cardverify',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 18, 13, 44, 12, 217117)),
        ),
    ]
