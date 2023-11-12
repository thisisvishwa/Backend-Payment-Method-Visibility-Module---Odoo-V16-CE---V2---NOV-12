```python
from odoo import models, fields, api

class PaymentMethodWizard(models.TransientModel):
    _name = 'payment.method.wizard'
    _description = 'Payment Method Wizard'

    payment_method_id = fields.Many2one('payment.method', string='Payment Method')
    payment_method_name = fields.Char(related='payment_method_id.name', string='Payment Method Name')
    payment_method_type = fields.Selection(related='payment_method_id.type', string='Payment Method Type')

    @api.multi
    def action_update_payment_method(self):
        self.ensure_one()
        active_ids = self._context.get('active_ids')
        if active_ids:
            orders = self.env['sale.order'].browse(active_ids)
            for order in orders:
                order.payment_method_id = self.payment_method_id.id
        return {'type': 'ir.actions.act_window_close'}
```