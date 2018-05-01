# -*- coding: utf-8 -*-
{
    'name': "citas_madl",

    'summary': """
        Citas de autores""",

    'description': """
        modulo de citas para la practica 4 de SGE
    """,

    'author': "Miguel Angel Dominguez Lopez",
    'website': "http://www.ingesoft.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'auto_install': False,
}
