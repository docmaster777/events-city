from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from location.models import City


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'object_user_category'
        verbose_name = "Категоря объекта"
        verbose_name_plural = "Категории объекта"

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     return super(Category, self).save(*args, **kwargs)

class ObjectUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', max_length=255)
    site = models.CharField(verbose_name='Сайт', max_length=255, blank=True, default='')
    address = models.TextField(verbose_name='Адрес', max_length=1000)
    longitude_coordinates = models.CharField(verbose_name='Координаты долготы', max_length=255, blank=True, default='')
    latitude_coordinates = models.CharField(verbose_name='Координаты широта', max_length=255, blank=True, default='')
    phone = models.CharField(verbose_name="Номер телефона", max_length=15, blank=True, default='')
    information = models.TextField(verbose_name='Дополнительная информация', max_length=1000, blank=True, default='')
    working_hours = models.CharField(verbose_name='Время работы', max_length=255, blank=True, default='')
    date_time_add = models.DateTimeField(verbose_name='Дата и время добавления', auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, max_length=100)
    description = models.TextField(blank=True, default='')
    email = models.EmailField(null=True, blank=True)

    STATUS_CHOICES = (
        ('Не активен', "Не активен"),
        ('Активен', "Активен"),
        ('На модерации', "На модерации"),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='На модерации', blank=True,
                              verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'object_user'
        verbose_name = "Объект пользователя"
        verbose_name_plural = "Объекты пользователей"
