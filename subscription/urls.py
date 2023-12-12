from django.urls import path

from subscription.api_views.subscription import SubscriptionCreateAPIView, SubscriptionDestroyAPIView, \
    SubscriptionListAPIView
from subscription.apps import SubscriptionConfig

app_name = SubscriptionConfig.name

urlpatterns = [
    path('subscription/list/', SubscriptionListAPIView.as_view(), name='subscription-list'),
    path('subscription/activate/', SubscriptionCreateAPIView.as_view(), name='subscription-activate'),
    path('subscription/deactivate/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription-deactivate'),
]
