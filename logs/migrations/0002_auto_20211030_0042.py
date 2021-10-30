# Generated by Django 3.2.7 on 2021-10-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardslogs',
            name='device_os',
            field=models.CharField(default='IoS 13', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cardslogs',
            name='device_ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='cardslogs',
            name='uuid',
            field=models.UUIDField(editable=False, null=True),
        ),
    ]