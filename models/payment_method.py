```python
from odoo import models, fields

class PaymentMethod(models.Model):
    _name = 'payment.method'
    _description = 'Payment Method'

    name = fields.Char(string='Payment Method Name', required=True)
    payment_type = fields.Selection([
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('paypal', 'PayPal'),
        ('other', 'Other'),
    ], string='Payment Type', required=True)
    details = fields.Text(string='Payment Method Details')
    active = fields.Boolean(string='Active', default=True)

    # Relations
    sale_order_ids = fields.One2many('sale.order', 'payment_method_id', string='Sales Orders')
    invoice_ids = fields.One2many('account.move', 'payment_method_id', string='Invoices')
    ecommerce_order_ids = fields.One2many('ecommerce.order', 'payment_method_id', string='eCommerce Orders')

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.name} ({record.payment_type})"
            result.append((record.id, name))
        return result
```