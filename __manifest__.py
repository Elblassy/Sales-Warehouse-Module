# -*- coding: utf-8 -*-
{
    'name': "Sales Warehouse",

    'summary': """
        This module is required to work with sales mobile app
        """,

    'description': """
        Add Warehouse id in users
    """,

    'author': "Elblasy",
    'website': "https://www.sst-egy.com",

    'category': 'Users',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

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
}