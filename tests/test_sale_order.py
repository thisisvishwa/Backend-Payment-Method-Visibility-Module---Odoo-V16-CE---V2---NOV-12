```python
from odoo.tests import common

class TestSaleOrder(common.TransactionCase):

    def setUp(self):
        super(TestSaleOrder, self).setUp()
        self.sale_order = self.env['sale.order']
        self.payment_method = self.env['payment.method']

    def test_payment_method_visibility(self):
        # Create a new sale order
        order = self.sale_order.create({
            'name': 'Test Order',
            'partner_id': self.env.ref('base.res_partner_1').id,
        })

        # Create a new payment method
        payment_method = self.payment_method.create({
            'name': 'Test Payment Method',
            'payment_type': 'credit_card',
        })

        # Assign the payment method to the sale order
        order.payment_method_id = payment_method.id

        # Check if the payment method is correctly assigned
        self.assertEqual(order.payment_method_id, payment_method)

    def test_payment_method_filtering_sorting(self):
        # Create multiple sale orders with different payment methods
        payment_method_1 = self.payment_method.create({'name': 'Payment Method 1', 'payment_type': 'cash'})
        payment_method_2 = self.payment_method.create({'name': 'Payment Method 2', 'payment_type': 'credit_card'})

        order_1 = self.sale_order.create({'name': 'Order 1', 'partner_id': self.env.ref('base.res_partner_1').id, 'payment_method_id': payment_method_1.id})
        order_2 = self.sale_order.create({'name': 'Order 2', 'partner_id': self.env.ref('base.res_partner_2').id, 'payment_method_id': payment_method_2.id})

        # Test filtering by payment method
        cash_orders = self.sale_order.search([('payment_method_id', '=', payment_method_1.id)])
        self.assertIn(order_1, cash_orders)
        self.assertNotIn(order_2, cash_orders)

        # Test sorting by payment method
        sorted_orders = self.sale_order.search([], order='payment_method_id')
        self.assertEqual(sorted_orders[0], order_1)
        self.assertEqual(sorted_orders[1], order_2)
```