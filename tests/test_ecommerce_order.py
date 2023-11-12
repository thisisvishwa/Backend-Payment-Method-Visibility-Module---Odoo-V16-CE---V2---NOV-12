```python
from odoo.tests import common

class TestEcommerceOrder(common.TransactionCase):

    def setUp(self):
        super(TestEcommerceOrder, self).setUp()
        self.EcommerceOrder = self.env['ecommerce.order']
        self.PaymentMethod = self.env['payment.method']

    def test_payment_method_visibility(self):
        # Create a new payment method
        new_payment_method = self.PaymentMethod.create({
            'name': 'Test Payment Method',
            'type': 'Credit Card',
        })

        # Create a new ecommerce order with the new payment method
        new_ecommerce_order = self.EcommerceOrder.create({
            'name': 'Test Order',
            'payment_method_id': new_payment_method.id,
        })

        # Check if the payment method is correctly set in the ecommerce order
        self.assertEqual(new_ecommerce_order.payment_method_id, new_payment_method)

    def test_payment_method_update(self):
        # Create a new payment method
        new_payment_method = self.PaymentMethod.create({
            'name': 'Test Payment Method',
            'type': 'Credit Card',
        })

        # Create a new ecommerce order with the new payment method
        new_ecommerce_order = self.EcommerceOrder.create({
            'name': 'Test Order',
            'payment_method_id': new_payment_method.id,
        })

        # Update the payment method in the ecommerce order
        new_payment_method_2 = self.PaymentMethod.create({
            'name': 'Test Payment Method 2',
            'type': 'Debit Card',
        })
        new_ecommerce_order.payment_method_id = new_payment_method_2

        # Check if the payment method is correctly updated in the ecommerce order
        self.assertEqual(new_ecommerce_order.payment_method_id, new_payment_method_2)

    def test_payment_method_filtering(self):
        # Create two new payment methods
        new_payment_method_1 = self.PaymentMethod.create({
            'name': 'Test Payment Method 1',
            'type': 'Credit Card',
        })
        new_payment_method_2 = self.PaymentMethod.create({
            'name': 'Test Payment Method 2',
            'type': 'Debit Card',
        })

        # Create two new ecommerce orders with different payment methods
        new_ecommerce_order_1 = self.EcommerceOrder.create({
            'name': 'Test Order 1',
            'payment_method_id': new_payment_method_1.id,
        })
        new_ecommerce_order_2 = self.EcommerceOrder.create({
            'name': 'Test Order 2',
            'payment_method_id': new_payment_method_2.id,
        })

        # Filter ecommerce orders by payment method
        filtered_orders = self.EcommerceOrder.search([('payment_method_id', '=', new_payment_method_1.id)])

        # Check if the filtering works correctly
        self.assertIn(new_ecommerce_order_1, filtered_orders)
        self.assertNotIn(new_ecommerce_order_2, filtered_orders)
```