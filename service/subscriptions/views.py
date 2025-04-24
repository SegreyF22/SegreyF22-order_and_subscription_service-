from rest_framework.viewsets import ModelViewSet
from .models import Tariff, UserSubscription
from .serializers import TariffSerializer, UserSubscriptionSerializer
from rest_framework.permissions import IsAuthenticated


class TariffViewSet(ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


class UserSubscriptionViewSet(ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserSubscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)