from django.contrib.auth.models import User
from django.db import models
from location.models import City

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Город")

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        db_table = 'user_profile'
