# Generated by Django 3.2.7 on 2021-12-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_issuingorginizationotp_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuingorginization',
            name='images',
            field=models.URLField(default='https://test.com', null=True),
        ),
    ]
