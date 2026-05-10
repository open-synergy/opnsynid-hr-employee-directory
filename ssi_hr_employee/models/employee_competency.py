# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class EmployeeCompetency(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a competency that can be associated with employees.

    Used as master data to define the catalog of behavioral and technical
    competencies required within the organization.
    """

    _name = "employee_competency"
    _inherit = ["mixin.master_data"]
    _description = "Employee Competency"
