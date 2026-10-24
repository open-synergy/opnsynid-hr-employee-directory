# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class HrJob(models.Model):  # pylint: disable=too-few-public-methods
    """
    Extension of the standard Job Position model.

    Adds job family level, computed allowed job grades, job grade assignments,
    and job description relationships to support the organizational grading
    and competency framework.
    """

    _inherit = ["hr.job"]

    @api.depends("job_family_level_id")
    def _compute_job_grade(self):
        """Compute the job grades allowed for the job position.

        ``allowed_job_grade_ids`` takes the grades of the selected job
        family level, or stays empty when no level is selected.
        """
        for job in self:
            result = False
            if job.job_family_level_id:
                result = job.job_family_level_id.job_grade_ids.ids
            job.allowed_job_grade_ids = result

    job_family_level_id = fields.Many2one(
        string="Job Family Level",
        comodel_name="hr.job_family_level",
    )
    allowed_job_grade_ids = fields.Many2many(
        string="Job Grades",
        comodel_name="hr.job_grade",
        compute="_compute_job_grade",
        compute_sudo=True,
        store=False,
    )
    job_grade_ids = fields.Many2many(
        string="Job Grades",
        comodel_name="hr.job_grade",
        relation="rel_job_2_grade",
        column1="job_id",
        column2="job_grade_id",
    )
    job_description_ids = fields.Many2many(
        string="Job Descriptions",
        comodel_name="job_description",
        relation="rel_job_position_2_job_description",
        column1="job_position_id",
        column2="job_description",
    )

    def onchange_job_family_level_id(self, job_family_level_id):
        """Build the onchange result for a job family level change.

        Start from the "before" value and domain, then replace them with
        the "after" ones when a job family level is selected.

        :param job_family_level_id: id of the selected
            ``hr.job_family_level``, or a falsy value when cleared
        :return: dict with ``value`` and ``domain`` keys
        """
        value = self._get_value_before_onchange_job_family_level_id()
        domain = self._get_domain_before_onchange_job_family_level_id()

        if job_family_level_id:
            obj_job_family_level = self.env["hr.job_family_level"]
            job_family_level = obj_job_family_level.browse([job_family_level_id])[0]
            value = self._get_value_after_onchange_job_family_level_id(job_family_level)
            domain = self._get_domain_after_onchange_job_family_level_id(
                job_family_level
            )
        return {"value": value, "domain": domain}

    def _get_value_before_onchange_job_family_level_id(self):
        """Return the values applied when no job family level is set.

        Extension point: override in a glue module to add values.

        :return: dict of field values, resetting ``job_grade_ids``
        """
        return {
            "job_grade_ids": [],
        }

    def _get_domain_before_onchange_job_family_level_id(self):
        """Return the domain applied when no job family level is set.

        Extension point: returns an empty domain by default.

        :return: dict of field domains, empty by default
        """
        return {}

    def _get_value_after_onchange_job_family_level_id(self, job_family_level):
        """Return the values applied when a job family level is set.

        Extension point: override in a glue module to add values.

        :param job_family_level: selected ``hr.job_family_level`` record
        :return: dict of field values, resetting ``job_grade_ids``
        """
        return {
            "job_grade_ids": [],
        }

    def _get_domain_after_onchange_job_family_level_id(self, job_family_level):
        """Return the domain applied when a job family level is set.

        Extension point: returns an empty domain by default.

        :param job_family_level: selected ``hr.job_family_level`` record
        :return: dict of field domains, empty by default
        """
        return {}
