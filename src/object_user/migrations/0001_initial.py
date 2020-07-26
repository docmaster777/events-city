# Generated by Django 3.0.8 on 2020-07-26 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'object_user_category',
            },
        ),
        migrations.CreateModel(
            name='ObjectUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('site', models.CharField(blank=True, default='', max_length=255, verbose_name='Сайт')),
                ('address', models.TextField(max_length=1000, verbose_name='Адрес')),
                ('longitude_coordinates', models.CharField(blank=True, default='', max_length=255, verbose_name='Координаты долготы')),
                ('latitude_coordinates', models.CharField(blank=True, default='', max_length=255, verbose_name='Координаты широта')),
                ('phone', models.CharField(blank=True, default='', max_length=15, verbose_name='Номер телефона')),
                ('information', models.TextField(blank=True, default='', max_length=1000, verbose_name='Дополнительная информация')),
                ('working_hours', models.CharField(blank=True, default='', max_length=255, verbose_name='Время работы')),
                ('date_time_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, default='')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('status', models.CharField(blank=True, choices=[('Не активен', 'Не активен'), ('Активен', 'Активен'), ('На модерации', 'На модерации')], default='На модерации', max_length=15, verbose_name='Статус')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.City')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'object_user',
            },
        ),
    ]
