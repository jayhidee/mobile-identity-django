# Generated by Django 3.2.7 on 2021-10-28 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_tokens', '0004_auto_20211028_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardtoken',
            name='date_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 28, 19, 48, 0, 949339)),
        ),
    ]
