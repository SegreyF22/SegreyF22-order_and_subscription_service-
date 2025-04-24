from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True, unique=True, verbose_name='Телефон')
    telegram_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='Телеграм ID')
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True, help_text='The groups this user belongs to')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True, help_text='Specific permissions for this user')

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Tariff(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название тарифа')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    class Meta:
        db_table = 'tariff'
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return f'Название тарифа: {self.name}'


class UserSubscription(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE, verbose_name='Тариф')
    active = models.BooleanField(default=True, verbose_name='Активна/Нет')

    class Meta:
        db_table = 'user_subscriptions'
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'Подписка пользователя: {self.user}'

