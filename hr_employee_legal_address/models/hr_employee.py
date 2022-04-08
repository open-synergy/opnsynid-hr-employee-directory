# -*- coding: utf-8 -*-
# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    legal_address_id = fields.Many2one(
        string="Legal Address",
        comodel_name="res.partner",
    )
    legal_street = fields.Char(
        string="Street",
        related="legal_address_id.street",
        store=True,
    )
    legal_street2 = fields.Char(
        string="Street2",
        related="legal_address_id.street2",
        store=True,
    )
    legal_zip = fields.Char(
        string="ZIP",
        related="legal_address_id.zip",
        store=True,
    )
    legal_city = fields.Char(
        string="City",
        related="legal_address_id.city",
        store=True,
    )
    legal_state_id = fields.Many2one(
        string="State",
        comodel_name="res.country.state",
        related="legal_address_id.state_id",
        store=True,
    )
    legal_country_id = fields.Many2one(
        string="Country",
        comodel_name="res.country",
        related="legal_address_id.country_id",
        store=True,
    )
    legal_phone = fields.Char(
        string="Phone",
        related="legal_address_id.phone",
        readonly=False,
        store=True,
    )

    @api.onchange(
        "address_home_id",
    )
    def onchange_legal_address_id(self):
        self.legal_address_id = False
