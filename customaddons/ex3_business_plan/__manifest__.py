# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Business plan',
    'version': '1.3',
    'sequence': 10,
    'description': """ """,
    'category': 'Productivity',
    'license': 'LGPL-3',
    'depends': ['sale', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/business_plan.xml',
        'views/order_line_inherit.xml',
        'views/plan_approve.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
