# Generated by Django 4.1.4 on 2023-01-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('personal_information', models.TextField()),
                ('education', models.TextField()),
                ('work_and_related_experience', models.TextField()),
                ('awards_and_honors', models.TextField()),
                ('activities_hobbies', models.TextField()),
                ('skills', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('time_added', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
