# Generated by Django 4.0 on 2022-10-17 19:32

import aproperty.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aproperty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Название лота')),
                ('slug', models.SlugField(verbose_name='Назваие в url')),
                ('price', models.CharField(help_text='Минимальная цена лота в комплексе', max_length=80, verbose_name='Цена лота')),
                ('addres', models.CharField(max_length=100, verbose_name='Адрес')),
                ('district', models.CharField(blank=True, default='', max_length=50, verbose_name='Округ')),
                ('subway', models.CharField(blank=True, default='', max_length=100, verbose_name='Метро')),
                ('lots_number', models.CharField(blank=True, default='по запросу', max_length=100, verbose_name='Кол-во лотов')),
                ('map_script', models.TextField(max_length=500, verbose_name='Скрипт карты')),
                ('min_square', models.BigIntegerField(default=10, verbose_name='Минимальная площядь')),
                ('max_square', models.BigIntegerField(default=500, verbose_name='Максимальная площядь')),
                ('short_phrase', models.TextField(help_text='Яркая и короткая фраза, отображается на странице лота', max_length=250, verbose_name='Короткая фраза')),
                ('description', models.TextField(help_text='Можно использовать html, до 1500 символов', max_length=1500, verbose_name='Полное описание лота')),
                ('title_image', models.ImageField(help_text='Фотография на странице лота', upload_to=aproperty.models.complex_dir_path, verbose_name='Обложка')),
                ('second_image', models.ImageField(blank=True, default=None, help_text='Первая фото в фотографиях комплекса', null=True, upload_to=aproperty.models.complex_dir_path, verbose_name='Доп. фото')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=aproperty.models.complex_dir_path, verbose_name='Логотип')),
                ('presentation', models.FileField(blank=True, default=None, null=True, upload_to=aproperty.models.complex_dir_path, verbose_name='Презентация лота')),
                ('click_amount', models.BigIntegerField(default=0, verbose_name='Кол-во нажатий')),
                ('main_order', models.IntegerField(default=0, help_text='Показываются все обьекты с не нулевыми значениями.', verbose_name='Порадок на главной странице')),
                ('is_published', models.BooleanField(default=True, help_text='Доступен ли обьект на сайте', verbose_name='Опубликован')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aproperty.area', verbose_name='Район')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aproperty.sitedata', verbose_name='Сайт')),
                ('specialist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aproperty.specialist', verbose_name='Специалист')),
            ],
            options={
                'verbose_name': 'Новостройка',
                'verbose_name_plural': 'Новостройки',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to=aproperty.models.complex_dir_path, verbose_name='Фото')),
                ('description', models.CharField(blank=True, default='', max_length=500, verbose_name='Описание')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary.primaryproperty', verbose_name='Обьект недвижимости')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['-name'],
            },
        ),
    ]
