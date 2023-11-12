```python
from odoo import models, fields

class Invoice(models.Model):
    _inherit = 'account.move'

    payment_method_id = fields.Many2one('payment.method', string='Payment Method')
    payment_method_name = fields.Char(related='payment_method_id.name', string='Payment Method Name', readonly=True)
    payment_method_type = fields.Selection(related='payment_method_id.type', string='Payment Method Type', readonly=True)

    def action_post(self):
        res = super(Invoice, self).action_post()
        self.update_payment_method_details()
        return res

    def update_payment_method_details(self):
        for record in self:
            payment_method = self.env['payment.method'].search([('invoice_id', '=', record.id)], limit=1)
            if payment_method:
                record.payment_method_id = payment_method.id
                record.payment_method_name = payment_method.name
                record.payment_method_type = payment_method.type
```
