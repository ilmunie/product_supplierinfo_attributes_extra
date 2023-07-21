# -*- coding: utf-8 -*-
{
    'name': 'product_supplierinfo_attributes_extra',
    'version': '1.0',
    'category': 'Purchase',
    'sequence': 15,
    'summary': 'Odoo v15 module that allows to configure extra costs in supplier pricelists based on product variant attribute values.',
    'description': "",
    'website': '',
    'depends': [
        'purchase',
    ],
    'data': [
        'views/product_supplierinfo_view.xml',
        'security/ir.model.access.csv',
    ],
   
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
