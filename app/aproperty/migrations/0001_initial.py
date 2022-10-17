# Generated by Django 4.0 on 2022-10-17 19:32

import aproperty.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
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
            name='SiteData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название сайта во вкладке', max_length=180, verbose_name='Заголовок')),
                ('title_image', models.ImageField(blank=True, default=None, help_text='Обложка для старта продаж', null=True, upload_to=aproperty.models.complex_dir_path1, verbose_name='Фото')),
                ('title_second', models.CharField(default='ПОРТАЛ ЭЛИТНОЙ НЕДВИЖИМОСТИ', help_text='Большая надпись в первой секции', max_length=180, verbose_name='Заголовок 1')),
                ('wh_link', models.CharField(default='https://wa.me/79818771062?text=Добрый день!%0AРасскажите, пожалуйста, подробнее о доступных ЖК', max_length=580, verbose_name='Ссылка WhatsApp')),
                ('meta_description', models.TextField(help_text='Описание сайта (для ссылко) CEO', max_length=500, verbose_name='Краткое описание')),
                ('scripts', models.TextField(max_length=1500, verbose_name='Скрипты аналитики')),
                ('header_phone', models.CharField(max_length=40, verbose_name='Телефон')),
                ('addres', models.TextField(max_length=400, verbose_name='Адрес')),
                ('footer_phones', models.TextField(max_length=400, verbose_name='Телефоны внизу')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'Данные сайта',
                'verbose_name_plural': 'Данные сайтов',
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
            name='YouTubeLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('link', models.CharField(max_length=400, verbose_name='Ссылка')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aproperty.sitedata')),
            ],
            options={
                'verbose_name': 'YouTube ссылка',
                'verbose_name_plural': 'YouTube ссылки',
            },
        ),
        migrations.CreateModel(
            name='MainSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=aproperty.models.complex_dir_path11, verbose_name='Фото')),
                ('logo', models.ImageField(upload_to=aproperty.models.complex_dir_path11, verbose_name='Лого')),
                ('link', models.CharField(max_length=400, verbose_name='Ссылка')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aproperty.sitedata')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=180, null=True, verbose_name='ФИО')),
                ('complex', models.CharField(max_length=180, verbose_name='Страница')),
                ('phone', models.CharField(blank=True, default=None, max_length=80, null=True, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, default=None, max_length=80, null=True, verbose_name='Email')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aproperty.sitedata', verbose_name='Сайт')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
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
        migrations.AddField(
            model_name='area',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aproperty.sitedata', verbose_name='Сайт'),
        ),
    ]
