# Generated by Django 3.0.8 on 2020-07-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object_user', '0004_auto_20200726_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]