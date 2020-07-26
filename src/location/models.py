from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=60, verbose_name="Название", unique=True)
    slug = models.SlugField(max_length=60, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        db_table = 'country'

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=60, verbose_name="Название", unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='Страны', verbose_name="Страна")

    class Meta:
        ordering = ['name']
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        db_table = 'region'

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=60, verbose_name="Название", unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='Регионы', verbose_name="Регион")

    class Meta:
        ordering = ['name']
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        db_table = 'city'

    def __str__(self):
        return self.name