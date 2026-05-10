# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class HrJobGrade(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a job grade used in the HR grading framework.

    Assigned to job positions and employees to indicate their compensation
    and responsibility level within the organization. Ordered by sequence
    to establish a grade hierarchy.
    """

    _name = "hr.job_grade"
    _inherit = ["mixin.master_data"]
    _description = "Job Grade"

    name = fields.Char(
        string="Job Grade",
    )
    category_id = fields.Many2one(
        string="Job Grade Category",
        comodel_name="hr.job_grade_category",
        required=False,
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
    )
