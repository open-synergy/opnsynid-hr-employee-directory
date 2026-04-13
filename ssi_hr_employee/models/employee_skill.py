# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class EmployeeSkill(models.Model):
    """
    Represents a skill that can be associated with employees.

    Used as master data to define the catalog of available employee
    skills in the organization.
    """

    _name = "employee_skill"
    _inherit = ["mixin.master_data"]
    _description = "Employee Skill"
