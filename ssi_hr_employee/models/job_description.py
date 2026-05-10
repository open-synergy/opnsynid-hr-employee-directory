# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class JobDescription(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a job description entry.

    Used as master data to define the responsibilities and tasks
    associated with job positions. Multiple descriptions can be linked
    to a single job position.
    """

    _name = "job_description"
    _inherit = ["mixin.master_data"]
    _description = "Job Description"
