from django.db import models
from subscriptions.models import CustomUser

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Покупатель')
    product_name = models.CharField(max_length=100 , verbose_name='Название товара')
    quantity = models.IntegerField(verbose_name='Количество')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Покупатель {self.user} | Заказ {self.product_name}'
