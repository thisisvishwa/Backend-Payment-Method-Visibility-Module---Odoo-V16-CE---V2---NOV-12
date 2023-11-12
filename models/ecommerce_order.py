```python
from odoo import models, fields

class EcommerceOrder(models.Model):
    _inherit = 'sale.order'

    payment_method_id = fields.Many2one('payment.method', string='Payment Method')
    payment_method_name = fields.Char(related='payment_method_id.name', string='Payment Method Name', store=True, readonly=True)
    payment_method_type = fields.Selection(related='payment_method_id.type', string='Payment Method Type', store=True, readonly=True)

    def action_confirm(self):
        res = super(EcommerceOrder, self).action_confirm()
        self.payment_method_id = self.env['payment.method'].search([('name', '=', self.payment_method_name)], limit=1)
        return res
```