# Generated by Django 3.2.7 on 2021-10-28 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_tokens', '0002_alter_cardtoken_officer'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardtoken',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 28, 15, 51, 32, 483315)),
        ),
        migrations.AddField(
            model_name='cardtoken',
            name='date_issued',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 10, 28, 15, 45, 53, 130162)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cardtoken',
            name='valied',
            field=models.BooleanField(default=True),
        ),
    ]
