# Generated by Django 4.0 on 2022-10-11 19:24

import aproperty.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Название района')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='ФИО')),
                ('phone', models.CharField(blank=True, default=None, max_length=80, null=True, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, default=None, max_length=80, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Название сета')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to=aproperty.models.complex_dir_path, verbose_name='Фото')),
                ('description', models.TextField(blank=True, default='', max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='ФИО')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to=aproperty.models.complex_dir_path, verbose_name='Фото')),
                ('role', models.CharField(max_length=180, verbose_name='Роль в проекте')),
                ('phone', models.CharField(max_length=18, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=40, verbose_name='Почта')),
                ('tg_link', models.CharField(max_length=250, verbose_name='Telegram ссылка')),
                ('wh_link', models.CharField(max_length=250, verbose_name='WhatsApp ссылка')),
            ],
            options={
                'verbose_name': 'Специалист',
                'verbose_name_plural': 'Специалисты',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='AreaPeculiarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('amount', models.IntegerField(default=0, verbose_name='Кол-во')),
                ('photo', models.ImageField(upload_to=aproperty.models.complex_dir_path, verbose_name='Фото')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aproperty.area', verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Особенность района',
                'verbose_name_plural': 'Особенности района',
                'ordering': ['-name'],
            },
        ),
    ]
