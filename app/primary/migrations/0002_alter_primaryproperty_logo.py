# Generated by Django 4.0 on 2022-11-12 21:23

import aproperty.models
from django.db import migrations, models
import primary.models


class Migration(migrations.Migration):

    dependencies = [
        ('primary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryproperty',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to=aproperty.models.complex_dir_path, validators=[primary.models.validate_logo], verbose_name='Логотип'),
        ),
    ]
