{
    'name': 'Enhanced Backend Payment Method Visibility',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': 'Enhanced visibility of payment methods in backend',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'sale',
        'account',
        'website_sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/payment_method_data.xml',
        'views/payment_method_view.xml',
        'views/sale_order_view.xml',
        'views/invoice_view.xml',
        'views/ecommerce_order_view.xml',
        'report/payment_method_report.xml',
        'wizard/payment_method_wizard_view.xml'
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'description': """
    Enhanced Backend Payment Method Visibility Module
    ------------------------------------------------
    This module provides enhanced visibility of payment methods used in eCommerce orders across various views in Odoo Version 16 Community Edition.
    """
}