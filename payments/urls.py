from payments.api_views.payment import PaymentViewSet
from payments.apps import PaymentsConfig
from rest_framework.routers import DefaultRouter

app_name = PaymentsConfig.name

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [

              ] + router.urls
