# Generated by Django 4.0 on 2022-10-16 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aproperty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='site',
        ),
        migrations.AlterModelOptions(
            name='sitedata',
            options={'verbose_name': 'Данные сайта', 'verbose_name_plural': 'Данные сайтов'},
        ),
    ]