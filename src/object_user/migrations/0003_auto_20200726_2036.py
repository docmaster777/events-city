# Generated by Django 3.0.8 on 2020-07-26 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('object_user', '0002_auto_20200726_2032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категоря объекта', 'verbose_name_plural': 'Категории объекта'},
        ),
        migrations.AlterModelOptions(
            name='objectuser',
            options={'verbose_name': 'Объект пользователя', 'verbose_name_plural': 'Объекты пользователей'},
        ),
    ]