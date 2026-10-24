# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class HrJobFamilyLevel(models.Model):
    """
    Represents a specific level within a job family.

    Combines a job family with a job family grade and narrows the allowable
    grade range to a min-max subset. Provides computed fields for the set of
    grades applicable at this level.
    """

    _name = "hr.job_family_level"
    _inherit = ["mixin.master_data"]
    _description = "Job Family Level"

    @api.depends(
        "job_family_id",
    )
    def _compute_job_grade(self):
        """Compute the grades allowed by the selected job family.

        Fills ``allowed_job_grade_ids`` with the grades of the job
        family, so the min and max grade can be restricted to them.
        """
        for jfl in self:
            jfl.allowed_job_grade_ids = jfl.job_family_id.job_grade_ids.ids

    @api.depends(
        "min_job_grade_id",
        "max_job_grade_id",
        "max_job_grade_id.sequence",
        "min_job_grade_id.sequence",
    )
    def _compute_job_grade_ids(self):
        """Compute the grades between the min and max grade.

        Fills ``job_grade_ids`` with every grade from ``min_job_grade_id``
        up to ``max_job_grade_id`` in the default grade order. The
        result is empty when either bound is not set.
        """
        obj_jg = self.env["hr.job_grade"]
        job_grade_ids = obj_jg.search([]).ids  # pylint: disable=no-search-all
        for jf in self:
            result = []
            if jf.min_job_grade_id and jf.max_job_grade_id:
                min_job_grade_id = jf.min_job_grade_id.id
                max_job_grade_id = jf.max_job_grade_id.id
                min_index = job_grade_ids.index(min_job_grade_id)
                max_index = job_grade_ids.index(max_job_grade_id)
                result = job_grade_ids[min_index : max_index + 1]
            jf.job_grade_ids = result

    name = fields.Char(
        required=False,
    )
    job_family_id = fields.Many2one(
        string="Job Family",
        comodel_name="hr.job_family",
        required=True,
    )
    job_family_grade_id = fields.Many2one(
        string="Job Family Grade",
        comodel_name="hr.job_family_grade",
        required=True,
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
        relation="rel_job_family_level_2_grade",
        column1="job_family_level_id",
        column2="job_grade_id",
        compute="_compute_job_grade_ids",
        compute_sudo=True,
        store=True,
    )
    min_job_grade_id = fields.Many2one(
        string="Min. Grade",
        comodel_name="hr.job_grade",
        required=True,
    )
    max_job_grade_id = fields.Many2one(
        string="Max. Grade",
        comodel_name="hr.job_grade",
        required=True,
    )

    def name_get(self):  # pylint: disable=deprecated-name-get
        """Return the display name of each job family level.

        The name is ``<family grade> <family> (<min> - <max>)``, where
        min and max are the first and last grade of ``job_grade_ids``.
        Both are shown as ``-`` when the level has no grades.

        :return: list of ``[id, name]`` pairs.
        :rtype: list
        """
        result = []
        for jfl in self:
            grade_count = len(jfl.job_grade_ids)
            if grade_count == 0:
                min_grade = "-"
                max_grade = "-"
            else:
                min_grade = jfl.job_grade_ids[0].name
                max_grade = jfl.job_grade_ids[grade_count - 1].name

            name = "%s %s (%s - %s)" % (  # pylint: disable=consider-using-f-string
                jfl.job_family_grade_id.name,
                jfl.job_family_id.name,
                min_grade,
                max_grade,
            )
            result.append([jfl.id, name])
        return result

    def onchange_job_family_id(self, job_family_id):
        """Build the value and domain for a changed job family.

        :param job_family_id: id of the selected job family, or False.
        :return: dict with the ``value`` and ``domain`` keys.
        :rtype: dict
        """
        value = self._get_value_before_onchange_job_family_id()
        domain = self._get_domain_before_onchange_job_family_id()

        if job_family_id:
            obj_job_family = self.env["hr.job_family"]
            job_family = obj_job_family.browse([job_family_id])[0]
            value = self._get_value_after_onchange_job_family_id(job_family)
            domain = self._get_domain_after_onchange_job_family_id(job_family)
        return {"value": value, "domain": domain}

    def _get_value_before_onchange_job_family_id(self):
        """Return the values applied when no job family is selected.

        Extension point; override it to add values.

        :return: dict of field values.
        :rtype: dict
        """
        return {
            "job_grade_ids": [],
        }

    def _get_domain_before_onchange_job_family_id(self):
        """Return the domain applied when no job family is selected.

        Extension point; override it to add domain entries.

        :return: dict of field domains.
        :rtype: dict
        """
        return {}

    def _get_value_after_onchange_job_family_id(self, job_family):
        """Return the values applied when a job family is selected.

        Extension point; override it to add values.

        :param job_family: the selected ``hr.job_family`` record.
        :return: dict of field values.
        :rtype: dict
        """
        return {
            "job_grade_ids": [],
        }

    def _get_domain_after_onchange_job_family_id(self, job_family):
        """Return the domain applied when a job family is selected.

        Extension point; override it to add domain entries.

        :param job_family: the selected ``hr.job_family`` record.
        :return: dict of field domains.
        :rtype: dict
        """
        return {}

    @api.constrains(
        "min_job_grade_id",
        "max_job_grade_id",
    )
    def _check_min_max_grade(self):
        """Ensure the min grade does not come after the max grade.

        :raises UserError: if the min grade is placed after the max
            grade in the default grade order.
        """
        obj_jg = self.env["hr.job_grade"]
        job_grade_ids = obj_jg.search([]).ids  # pylint: disable=no-search-all
        msg = _("Wrong Max Min Grade")
        for jf in self:
            if jf.min_job_grade_id and jf.max_job_grade_id:
                min_job_grade_id = jf.min_job_grade_id.id
                max_job_grade_id = jf.max_job_grade_id.id
                min_index = job_grade_ids.index(min_job_grade_id)
                max_index = job_grade_ids.index(max_job_grade_id)
                if min_index > max_index:
                    raise UserError(msg)
