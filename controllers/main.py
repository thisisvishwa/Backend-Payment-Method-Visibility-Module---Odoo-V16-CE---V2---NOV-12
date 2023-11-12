```python
from odoo import http
from odoo.http import request

class MainController(http.Controller):

    @http.route('/payment_method/details', type='json', auth='user')
    def get_payment_method_details(self, **kwargs):
        payment_method_id = kwargs.get('payment_method_id')
        payment_method = request.env['payment.method'].browse(payment_method_id)
        return {
            'id': payment_method.id,
            'name': payment_method.name,
            'type': payment_method.type,
        }

    @http.route('/payment_method/update', type='json', auth='user')
    def update_payment_method(self, **kwargs):
        payment_method_id = kwargs.get('payment_method_id')
        payment_method = request.env['payment.method'].browse(payment_method_id)
        payment_method.write(kwargs)
        return {'status': 'success'}

    @http.route('/payment_method/filter', type='json', auth='user')
    def filter_payment_methods(self, **kwargs):
        domain = []
        if kwargs.get('payment_method_type'):
            domain.append(('type', '=', kwargs.get('payment_method_type')))
        payment_methods = request.env['payment.method'].search(domain)
        return [{'id': pm.id, 'name': pm.name, 'type': pm.type} for pm in payment_methods]
```