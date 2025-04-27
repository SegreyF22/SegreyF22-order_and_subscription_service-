import telebot
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializers

bot = telebot.TeleBot('8083153363:AAFLITTlPQayAY98yx724nxKaGu1844dx4A')


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        bot.send_message(self.request.user.telegram_id, f'Вам пришел новый заказ!')
