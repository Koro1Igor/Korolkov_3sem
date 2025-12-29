from abc import ABC, abstractmethod

# ===== Strategy (поведенческий паттерн) =====
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class CardPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} by card"


class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} via PayPal"


# ===== Factory Method (порождающий паттерн) =====
class PaymentFactory:
    @staticmethod
    def create_payment(method: str) -> PaymentStrategy:
        if method == "card":
            return CardPayment()
        if method == "paypal":
            return PayPalPayment()
        raise ValueError("Unknown payment method")


# ===== Decorator (структурный паттерн) =====
class Order:
    def cost(self) -> float:
        return 100.0


class OrderDecorator(Order):
    def __init__(self, order: Order):
        self._order = order

    def cost(self) -> float:
        return self._order.cost()


class GiftWrapDecorator(OrderDecorator):
    def cost(self) -> float:
        return self._order.cost() + 10.0


# ===== Контекст =====
class CheckoutService:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def checkout(self, order: Order) -> str:
        return self.payment_strategy.pay(order.cost())
