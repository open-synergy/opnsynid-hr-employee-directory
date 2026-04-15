# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class HrEmployee(models.Model):  # pylint: disable=too-few-public-methods
    """
    Extends hr.employee with operating unit support.
    Adds mixin.single_operating_unit so employee records
    can be scoped to a specific operating unit.
    """

    _name = "hr.employee"
    _inherit = [
        "hr.employee",
        "mixin.single_operating_unit",
    ]
