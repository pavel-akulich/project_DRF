from django.contrib import admin

from payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'payment_date', 'course', 'lesson', 'payment_amount', 'payment_method',)
