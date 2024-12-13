# -*- coding: utf-8 -*-
{
    "name": "Employee Cash Move of Sale Session",
    "version": "16.0.1",
    "category": "Sales/Point of Sale",
    'summary': "Allow employees cash to move in POS",
    'description': "Allow employees cash to move in POS",
    "author": "Grupo Hernandez S.U.R.L",
    "website": "https://www.grupohernandez.cu",
    "auto_install": False,
    "depends": ["point_of_sale", "pos_hr"],
    'installable': True,
    'assets': {
        'point_of_sale.assets': [
            'pos_employee_cash_move/static/src/js/Chrome.js',
            ],
    },
    'images': ['static/description/icon.png'],
    'license': 'LGPL-3',
}
