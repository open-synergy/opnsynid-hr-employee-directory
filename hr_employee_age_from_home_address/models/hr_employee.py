# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    age_year = fields.Integer(
        string="Age Year",
        related="address_home_id.age_year",
        store=True,
    )
    age_month = fields.Integer(
        string="Age Month",
        related="address_home_id.age_month",
        store=True,
    )
    age_day = fields.Integer(
        string="Age Day",
        related="address_home_id.age_day",
        store=True,
    )
