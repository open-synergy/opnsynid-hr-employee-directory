# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class HrJobGradeCategory(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a category grouping multiple job grades.

    Used to classify and organize job grades into broader compensation
    or responsibility bands within the grading framework.
    """

    _name = "hr.job_grade_category"
    _inherit = ["mixin.master_data"]
    _description = "Job Grade Category"

    name = fields.Char(
        string="Job Grade Category",
    )
