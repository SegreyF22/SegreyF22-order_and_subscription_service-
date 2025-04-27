from rest_framework.routers import DefaultRouter
from .views import TariffViewSet, UserSubscriptionViewSet

router = DefaultRouter()
router.register('tariffs', TariffViewSet, basename='tariffs')
router.register('subscriptions', UserSubscriptionViewSet, basename='subscriptions')

urlpatterns = router.urls
