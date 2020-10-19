# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'EDI Document Synchonizaton Base',
    'version': '1.0',
    'category': 'Tools',
    'description': """
Allows you to configure edi document exchnage configurations
==============================================================
You can your own edi xml expoert and import via ftp.
""",
    'depends': ['mail'],
    'data': [
        'security/base_edi_security.xml',
        'security/ir.model.access.csv',
        'views/edi_config_view.xml',
        #'views/res_partner_view.xml',
    ],
    'demo': [],
    'installable': True,
}
