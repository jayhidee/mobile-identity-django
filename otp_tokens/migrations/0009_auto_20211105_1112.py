# Generated by Django 3.2.7 on 2021-11-05 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_tokens', '0008_auto_20211031_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardtoken',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 12, 12, 24, 254414)),
        ),
        migrations.AlterField(
            model_name='cardverify',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 11, 18, 24, 255310)),
        ),
    ]
