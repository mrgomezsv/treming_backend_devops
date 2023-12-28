# -*- coding: utf-8 -*-
{
    'name': "Treming Backend DevOps",
    'summary': """
        Entorno Backend""",
    'description': """
        Entorno de Administracion DevOps
    """,
    'author': "Grupo Treming",
    'website': "https://www.treming.com",
    'category': 'Tools',
    'version': '0.1',
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/backend_tr.xml',
    ],
}
