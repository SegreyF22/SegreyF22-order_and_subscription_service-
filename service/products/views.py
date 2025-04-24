from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializers
import os
import requests


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return Order.objects.filter(user=self.request.user)
        return Order.objects.all()

    def perform_create(self, serializer):
        order = serializer.save(user=self.request.user)
        self.notify_telegram(self.request.user)

    def notify_telegram(self, user):
        if user.telegram_id:
            requests.post(f"https://api.telegram.org/bot{os.environ['TELEGRAM_TOKEN']}/sendMessage",
                data={
                    "chat_id": user.telegram_id,
                    "text": "Вам пришёл новый заказ!"
                })