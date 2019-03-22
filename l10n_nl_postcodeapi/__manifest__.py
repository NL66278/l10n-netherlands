# -*- coding: utf-8 -*-
# Copyright 2013-2019 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Integration with PostcodeApi.nu',
    'summary': 'Autocomplete Dutch addresses using PostcodeApi.nu',
    'version': '10.0.0.2.0',
    'author': 'Therp BV,Odoo Community Association (OCA)',
    'category': 'Localization',
    'website': 'https://github.com/OCA/l10n-netherlands',
    'license': 'AGPL-3',
    'depends': ['partner_street_number'],
    'data': [
        'data/ir_config_parameter.xml',
        ],
    # Temporarily an embedded version of the pyPostcode library will be used
    # by this module, because of severe shortcomings in the present version
    # of the code, especially the lack of decent error-handling.
    'external_dependencies': {
        'python': ['pyPostcode'],
    },
    'installable': True,
}
