import unittest
from unittest.mock import Mock
from shop import (
    PaymentFactory,
    GiftWrapDecorator,
    Order,
    CheckoutService
)


class TestShop(unittest.TestCase):

    def test_factory_creates_card_payment(self):
        payment = PaymentFactory.create_payment("card")
        self.assertEqual(payment.pay(100), "Paid 100 by card")

    def test_decorator_adds_cost(self):
        order = GiftWrapDecorator(Order())
        self.assertEqual(order.cost(), 110.0)

    def test_checkout_with_mock_payment(self):
        mock_payment = Mock()
        mock_payment.pay.return_value = "Mock payment success"

        service = CheckoutService(mock_payment)
        result = service.checkout(Order())

        mock_payment.pay.assert_called_once()
        self.assertEqual(result, "Mock payment success")


if __name__ == "__main__":
    unittest.main()
