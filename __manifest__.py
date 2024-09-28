# -*- coding: utf-8 -*-
# Copyright 2024 ASAid Group Investment - Fatchul Bari Hikmawan
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    'name': "ASAid Carousel Extension",
    'summary': "Add various additional custom options or features for the Carousel block",
    'description': """
        ASAid Carousel Extension is an Odoo 17 module that enhances the functionality of website Carousels. It add various additional custom options or features for the Carousel block.
    """,
    'author': "ASAid Group Investment",
    'website': "https://www.asaidgroup.com",
    "license": "LGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['web_editor','website'],

    # always loaded
    'data': [
        'views/carousel_options_extension.xml',
    ],
}

