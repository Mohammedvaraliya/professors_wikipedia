# Generated by Django 4.1.4 on 2023-01-01 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='time_added',
            field=models.TimeField(auto_now=True),
        ),
    ]
