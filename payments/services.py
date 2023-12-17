from enum import Enum

import stripe


class Currency(Enum):
    """Класс для хранения валют"""
    USD = 'usd'
    EUR = 'eur'


class StripeService:
    """Класс для работы с платежным сервисом Stripe"""

    def __init__(self, api_key):
        """
        Инициализирует экземпляр класса StripeService
        """
        self.__stipe = stripe
        self.__stipe.api_key = api_key

    def create_payment(self, amount: int, currency: Currency = Currency.USD):
        """
        Создает платежный запрос к сервису Stripe для создания платежного намерения
        """
        data = self.__stipe.PaymentIntent.create(
            amount=amount,
            currency=currency.value,
            automatic_payment_methods={"enabled": True}
        )

        return data
