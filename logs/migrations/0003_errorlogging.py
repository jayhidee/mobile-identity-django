# Generated by Django 3.2.7 on 2021-11-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_auto_20211030_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorLogging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('error_type', models.CharField(max_length=255)),
                ('error_details', models.TextField()),
                ('time_field', models.TimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['time_field'],
            },
        ),
    ]
