from django.http import JsonResponse
from subscriptions.models import UserSubscription


class SubscriptionCheckMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request ,*args, **kwargs):
        if request.path.startswith('/products/'):
            if request.user.is_authenticated:
                try:
                    subscription = UserSubscription.objects.get(user=request.user)
                    if not subscription.active:
                        return JsonResponse({'error': 'Необходимо оформить подписку'}, status=403)
                except UserSubscription.DoesNotExist:
                    return JsonResponse({'error': 'Подписка отсутствует'}, status=403)
        return self.get_response(request)