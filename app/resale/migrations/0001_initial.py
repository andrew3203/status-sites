# Generated by Django 4.0 on 2022-10-17 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('primary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResaleProperty',
            fields=[
                ('primaryproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='primary.primaryproperty')),
                ('rooms_number', models.IntegerField(blank=True, default=None, null=True, verbose_name='Кол-во комнат')),
                ('floor', models.IntegerField(blank=True, default=None, null=True, verbose_name='Этаж')),
                ('floor_number', models.IntegerField(blank=True, default=None, null=True, verbose_name='Кол-во этажей в доме')),
                ('decor', models.CharField(blank=True, default=None, max_length=80, null=True, verbose_name='Ремонт')),
                ('construction_year', models.DateField(blank=True, default=None, null=True, verbose_name='Год постройки')),
                ('bulding_material', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Тип (материал) дома')),
                ('ceiling_height', models.FloatField(blank=True, default=None, null=True, verbose_name='Высота потолков')),
                ('elevators', models.IntegerField(blank=True, default=None, null=True, verbose_name='Пассажирских лифтов')),
                ('freight_elevators', models.IntegerField(blank=True, default=None, null=True, verbose_name='Грузовых лифтов')),
                ('parking', models.BooleanField(default=False, verbose_name='Парковка')),
                ('ownership', models.IntegerField(blank=True, default=None, null=True, verbose_name='Форма собственности')),
                ('entrances', models.IntegerField(blank=True, default=None, null=True, verbose_name='Кол во подъездов')),
                ('rooms_on_floor', models.IntegerField(blank=True, default=None, null=True, verbose_name='Квартир на этаже')),
                ('penthouse', models.BooleanField(default=False, verbose_name='Пентхаус')),
                ('terrace', models.BooleanField(default=False, verbose_name='Терраса')),
                ('rooms_in_hous', models.IntegerField(blank=True, default=None, null=True, verbose_name='Квартир в доме')),
                ('window_to', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Окна выходят')),
            ],
            options={
                'verbose_name': 'Втричная недвижимость',
                'verbose_name_plural': 'Втричная недвижимость',
                'ordering': ['-name'],
            },
            bases=('primary.primaryproperty',),
        ),
    ]
