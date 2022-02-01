# Generated by Django 3.2.7 on 2022-01-31 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_tokens', '0030_auto_20220129_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardtoken',
            name='hash',
            field=models.CharField(default='s', max_length=220),
        ),
        migrations.AlterField(
            model_name='cardtoken',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 31, 21, 22, 51, 857937)),
        ),
        migrations.AlterField(
            model_name='cardverify',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 31, 20, 28, 51, 858616)),
        ),
    ]