# Generated by Django 4.0 on 2022-11-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aproperty', '0002_livingtype'),
        ('resale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resaleproperty',
            name='living_type',
            field=models.ManyToManyField(blank=True, default=None, to='aproperty.LivingType', verbose_name='Тип жилья'),
        ),
    ]