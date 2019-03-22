.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================================
Auto-completion for Dutch addresses
===================================

This module contains integration of the excellent and free address completion
service 'PostcodeAPI'. The service allows lookups by zip code and house number,
providing street name and city. The lookups will be triggered in the partner
form views when a zip code or house number is entered or modified. Only
Dutch addresses (which is assumed to include addresses with no country) are
auto-completed.

More info about the lookup service here: http://www.postcodeapi.nu/

The check on zipcode will not throw Errors in the user-interface, for
conditons like invalid or not set Api key parameter, failing connections,
or errors like the maximum number of lookups done. But these will cause
warnings or errors in the log. User preventable errors, like wrong zipcodes
will lead to validation errors.

Installation
============
This module depends on the module partner_street_number, which will split
up the street field into separate fields for street name and number.

This module can be gotten from https://github.com/oca/partner-contact/tree/10.0

You also need to have the 'pyPostcode' Python library by Stefan Jansen
installed (https://pypi.python.org/pypi/pyPostcode).

Configuration
=============
Please enter the API key that you request from PostcodeAPI into the system
parameter 'l10n_nl_postcodeapi.apikey'

Provinces are autocompleted if a country state with the exact name is found in
the system. This module is not directly dependent on l10n_nl_country_states,
but it is advisable to install that module to make sure all dutch
provinces (contry states) are in the database.

Compatibility
=============
This module is compatible with Odoo 10.0.

Usage
=====

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/176/10.0


Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-netherlands/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and
welcomed feedback.

Credits
=======

Contributors
------------

* Stefan Rijnhart (Therp BV) <stefan@therp.nl>
* Ronald Portier (Therp BV) <ronald@therp.nl>

Maintainer
----------

.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA at https://github.com/OCA/l10n-netherlands

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
