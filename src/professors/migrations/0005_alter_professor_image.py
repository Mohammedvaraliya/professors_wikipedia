# Generated by Django 4.1.4 on 2023-01-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0004_professor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='professor_images'),
        ),
    ]
