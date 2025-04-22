from django.contrib import admin
from subscriptions.models import CustomUser, Tariff, UserSubscription

admin.site.register(CustomUser)
admin.site.register(Tariff)
admin.site.register(UserSubscription)
