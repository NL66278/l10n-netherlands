# -*- coding: utf-8 -*-
# Copyright 2013-2019 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# pylint: disable=attribute-defined-outside-init,invalid-name,missing-docstring
import logging

from odoo import api, exceptions, models, _


_logger = logging.getLogger(__name__)  # pylint: disable=invalid-name

try:
    from ..pyPostcode.api import Api
    from ..pyPostcode.exceptions import \
        PostcodeException, PostcodeBadArgumentError, PostcodeValidationError
except:  # pylint: disable=bare-except
    _logger.warn(_("pyPostcode not found, postcode API disabled."))
    Api = None


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def get_provider_obj(self):
        if not Api:
            # pyPostcode not installed
            return False
        apikey = self.env['ir.config_parameter'].get_param(
            'l10n_nl_postcodeapi.apikey', '').strip()
        if not apikey or apikey == 'Your API key':
            return False
        return Api(apikey)

    @api.model
    def get_province(self, province):
        """ Return the id for a province name or False."""
        if not province:
            return False
        country_state = self.env['res.country.state'].search(
            [('name', '=', province)], limit=1)
        return country_state[0].id if country_state else False

    @api.onchange('zip', 'street_number', 'country_id')
    def on_change_zip_street_number(self):
        """
        Normalize the zip code, check on the partner's country and
        if all is well, request address autocompletion data.

        NB. postal_code is named 'zip' in Odoo, but is this a reserved
        keyword in Python
        """
        if not Api:
            return
        postal_code = self.zip and self.zip.replace(' ', '').upper()
        country = self.country_id
        if not (postal_code and self.street_number) or \
                country and country != self.env.ref('base.nl'):
            return
        try:
            provider_obj = self.get_provider_obj()
            if not provider_obj:
                return
            pc_info = provider_obj.get_postcode_info(
                postal_code, self.street_number)
            self.street_name = pc_info.street
            self.city = pc_info.town
            self.state_id = self.get_province(pc_info.province)
        except (PostcodeBadArgumentError, PostcodeValidationError) as pc_exc:
            raise exceptions.ValidationError(pc_exc.message)
        except PostcodeException as pc_exc:
            _logger.exception(
                _("Error in communicating with Postcode API: %s"),
                pc_exc.message)
