```python
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_method_id = fields.Many2one('payment.method', string='Payment Method')
    payment_method_name = fields.Char(related='payment_method_id.name', string='Payment Method Name', store=True, readonly=True)
    payment_method_type = fields.Selection(related='payment_method_id.type', string='Payment Method Type', store=True, readonly=True)

    @api.onchange('payment_method_id')
    def _onchange_payment_method_id(self):
        self.payment_method_name = self.payment_method_id.name
        self.payment_method_type = self.payment_method_id.type

    @api.model
    def create(self, vals):
        order = super(SaleOrder, self).create(vals)
        order._onchange_payment_method_id()
        return order

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        if 'payment_method_id' in vals:
            self._onchange_payment_method_id()
        return res
```