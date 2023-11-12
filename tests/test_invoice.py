```python
from odoo.tests import common

class TestInvoice(common.TransactionCase):

    def setUp(self):
        super(TestInvoice, self).setUp()
        self.invoice = self.env['account.move']
        self.payment_method = self.env['payment.method']

    def test_payment_method_visibility(self):
        # Create a new invoice
        new_invoice = self.invoice.create({
            'name': 'Test Invoice',
            'type': 'out_invoice',
            'partner_id': self.env.ref('base.res_partner_2').id,
        })

        # Create a new payment method
        new_payment_method = self.payment_method.create({
            'name': 'Test Payment Method',
            'description': 'This is a test payment method',
        })

        # Assign the payment method to the invoice
        new_invoice.payment_method_id = new_payment_method.id

        # Check if the payment method is correctly assigned
        self.assertEqual(new_invoice.payment_method_id, new_payment_method, "Payment method not correctly assigned to invoice")

    def test_payment_method_filtering_sorting(self):
        # Test code for advanced filtering and sorting based on payment methods goes here

    def test_payment_method_customizable_display(self):
        # Test code for customizable display of payment method details goes here

    def test_payment_method_integration(self):
        # Test code for integration with core modules goes here

    def test_payment_method_security(self):
        # Test code for role-based access control and encryption of sensitive payment data goes here
```