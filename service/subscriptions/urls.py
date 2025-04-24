from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TariffViewSet, UserSubscriptionViewSet

router = DefaultRouter()
router.register('tariffs', TariffViewSet)
router.register('subscriptions',UserSubscriptionViewSet)

urlpatterns = [
    path('',include(router.urls)),
]