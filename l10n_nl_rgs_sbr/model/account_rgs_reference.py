# -*- coding: utf-8 -*-
"""Define model account.rgs.reference."""
##############################################################################
#
#    Copyright (C) 2015 Therp BV <http://therp.nl>.
#
#    All other contributions are (C) by their respective contributors
#
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields


class AccountRgsReference(models.Model):
    """Define model account.rgs.reference."""
    _name = 'account.rgs.reference'
    _description = 'Code and descriptions for "Referentie Grootboek Schema".'
    _order = 'code'

    code = fields.Char(string='Reference code')
    name = fields.Char(string='Description')

    _sql_constraints = [
        (
            'code__uniq',
            'unique (code)',
            'The reference code must be unique!'
        ),
    ]

    def name_search(
            self, cr, uid, name, args=None, operator='ilike', context=None,
            limit=100):
        """Search for first for code, then for name."""
        if not args:
            args = []
        args = args[:]
        ids = []
        if name:
            # First seach for exact code:
            ids = self.search(
                cr, uid, [('code', '=', name),], context=context,
                limit=limit
            )
            if not ids:
                # Now traditional name search:
                ids = self.search(
                    cr, uid, [('name', operator, name),] + args,
                    context=context, limit=limit
                )
        if not ids:
            ids = self.search(cr, uid, args, context=context, limit=limit)
        return self.name_get(cr, uid, ids, context=context)

    def name_get(self, cr, uid, ids, context=None):
        """Name consists of code followed by description."""
        if not ids:
            return []
        if isinstance(ids, (int, long)):
                    ids = [ids]
        reads = self.read(cr, uid, ids, ['name', 'code'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['code']:
                name = record['code'] + ' ' + name
            res.append((record['id'], name))
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
