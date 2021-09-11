# -*- coding: utf-8 -*-
{
    'name': "Transportation",
    'summary': """ transportation management""",
    'description': """
       This module was created for the purpose of creating a place to manage the company's means of transporting goods in and out of warehouses.

    """,
    'website': "https://www.facebook.com/profile.php?id=100043023576264",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': -100,
    'author': "DoDucAnh",

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
