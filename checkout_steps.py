from behave import given, when, then
from shop import (
    Order,
    GiftWrapDecorator,
    PaymentFactory,
    CheckoutService
)

@given("an order with gift wrap")
def step_order(context):
    context.order = GiftWrapDecorator(Order())

@when("I pay by card")
def step_pay(context):
    payment = PaymentFactory.create_payment("card")
    service = CheckoutService(payment)
    context.result = service.checkout(context.order)

@then("the payment result should be successful")
def step_result(context):
    assert "Paid" in context.result
