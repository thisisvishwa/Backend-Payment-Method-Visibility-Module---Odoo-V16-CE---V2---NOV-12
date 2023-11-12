```python
from odoo import http
from odoo.http import request

class PaymentMethodAPI(http.Controller):

    @http.route('/api/payment_methods', type='json', auth='user')
    def get_payment_methods(self, **kwargs):
        payment_methods = request.env['payment.method'].search([])
        return {
            'payment_methods': [method.name for method in payment_methods]
        }

    @http.route('/api/payment_methods/<int:payment_method_id>', type='json', auth='user')
    def get_payment_method_details(self, payment_method_id, **kwargs):
        payment_method = request.env['payment.method'].browse(payment_method_id)
        return {
            'payment_method_details': {
                'id': payment_method.id,
                'name': payment_method.name,
                'type': payment_method.type,
            }
        }

    @http.route('/api/payment_methods/update', type='json', auth='user', methods=['POST'])
    def update_payment_method(self, **kwargs):
        payment_method_id = kwargs.get('payment_method_id')
        new_details = kwargs.get('new_details')
        payment_method = request.env['payment.method'].browse(payment_method_id)
        payment_method.write(new_details)
        return {
            'status': 'success',
            'message': 'Payment method updated successfully'
        }
```