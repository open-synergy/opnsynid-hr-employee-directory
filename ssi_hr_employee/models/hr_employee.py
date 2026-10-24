# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class HrEmployeeBase(models.AbstractModel):
    """
    Extension of hr.employee.base with additional HR directory fields.

    Adds employment status, job grade, organization unit, legal address,
    join/termination/contract dates, and work longevity computation to
    the base employee abstract model.
    """

    _inherit = "hr.employee.base"

    @api.depends("job_id")
    def _compute_job_grade(self):
        """Compute the job grades allowed for the employee's job.

        Set ``allowed_job_grade_ids`` to the grades of ``job_id``, or to
        empty when no job is selected.
        """
        for employee in self:
            result = False
            if employee.job_id:
                result = employee.job_id.job_grade_ids.ids
            employee.allowed_job_grade_ids = result

    employment_status_id = fields.Many2one(
        string="Employment Status",
        comodel_name="hr.employment_status",
    )
    job_grade_id = fields.Many2one(
        string="Job Grade",
        comodel_name="hr.job_grade",
        required=False,
    )
    allowed_job_grade_ids = fields.Many2many(
        string="Job Grades",
        comodel_name="hr.job_grade",
        compute="_compute_job_grade",
        compute_sudo=True,
        store=False,
    )
    organization_unit_id = fields.Many2one(
        string="Organization Unit", comodel_name="hr.department"
    )
    main_job_description_ids = fields.Many2many(
        string="Main Job Description",
        comodel_name="job_description",
        related="job_id.job_description_ids",
        compute_sudo=True,
    )

    @api.onchange("organization_unit_id")
    def onchange_department_id(self):
        """Reset the department and restrict its domain to the unit.

        Triggered by ``organization_unit_id``. When an organization unit
        is selected, ``department_id`` is cleared and its domain is
        limited to the unit and its child departments.

        :return: dict with the ``domain`` for ``department_id``
        """
        domain = {}
        if self.organization_unit_id:
            self.department_id = False  # pylint: disable=attribute-defined-outside-init
            domain = {
                "department_id": [("id", "child_of", [self.organization_unit_id.id])]
            }
        return {"domain": domain}

    legal_address_id = fields.Many2one(
        string="Legal Address",
        comodel_name="res.partner",
    )
    legal_street = fields.Char(
        string="Street",
        related="legal_address_id.street",
        compute_sudo=True,
        store=True,
    )
    legal_street2 = fields.Char(
        string="Street2",
        related="legal_address_id.street2",
        compute_sudo=True,
        store=True,
    )
    legal_zip = fields.Char(
        string="ZIP",
        related="legal_address_id.zip",
        compute_sudo=True,
        store=True,
    )
    legal_city = fields.Char(
        string="City",
        related="legal_address_id.city",
        compute_sudo=True,
        store=True,
    )
    legal_state_id = fields.Many2one(
        string="State",
        comodel_name="res.country.state",
        related="legal_address_id.state_id",
        compute_sudo=True,
        store=True,
    )
    legal_country_id = fields.Many2one(
        string="Country",
        comodel_name="res.country",
        related="legal_address_id.country_id",
        compute_sudo=True,
        store=True,
    )
    legal_phone = fields.Char(
        string="Phone",
        related="legal_address_id.phone",
        compute_sudo=True,
        readonly=True,
        store=True,
    )

    date_join = fields.Date(
        string="Join Date",
    )
    date_termination = fields.Date(
        string="Termination Date",
    )
    date_permanent = fields.Date(
        string="Permanent Date",
    )
    date_contract_start = fields.Date(
        string="Contract Start Date",
    )
    date_contract_end = fields.Date(
        string="Contract End Date",
    )
    year_work_longetivity = fields.Integer(
        string="Year Work Longetivity",
        compute="_compute_work_longetivity",
        compute_sudo=True,
        store=True,
    )
    month_work_longetivity = fields.Integer(
        string="Month Work Longetivity",
        compute="_compute_work_longetivity",
        compute_sudo=True,
        store=True,
    )

    @api.depends(
        "date_join",
        "date_termination",
    )
    def _compute_work_longetivity(self):
        """Compute the years and months of work longevity.

        The period runs from ``date_join`` to ``date_termination``, or to
        today when the employee has not been terminated. Both results
        are zero when ``date_join`` is empty.
        """
        for document in self:
            year_work = month_work = 0
            if document.date_join:
                if not document.date_termination:
                    dt_termination = date.today()
                else:
                    dt_termination = document.date_termination
                    # datetime.strptime(document.date_termination, "%Y-%m-%d")
                dt_join = document.date_join
                # datetime.strptime(document.date_join, "%Y-%m-%d")
                year_work = relativedelta(dt_termination, dt_join).years
                month_work = relativedelta(dt_termination, dt_join).months
            document.year_work_longetivity = year_work
            document.month_work_longetivity = month_work

    @api.model
    def cron_update_longetivity(self):
        """Recompute the work longevity of every employee.

        Called by the scheduled action so the stored longevity values
        follow the passing of time, since ``date.today()`` is not a
        compute dependency.
        """
        employee_ids = self.search([])  # pylint: disable=no-search-all
        for employee in employee_ids:
            employee._compute_work_longetivity()

    def action_dummy_save(self):
        """Do nothing so the form is saved by the button click.

        :return: ``True``
        """
        return True

    @api.constrains(
        "date_contract_start",
        "date_contract_end",
    )
    def _check_date_contract_start_end(self):
        """Validate that the contract ends after it starts.

        :raises UserError: if ``date_contract_end`` is earlier than
            ``date_contract_start``
        """
        for record in self:
            if record.date_contract_start and record.date_contract_end:
                strWarning = _(  # pylint: disable=invalid-name
                    "Contract End Date must be greater than Contract Start Date"
                )
                if record.date_contract_end < record.date_contract_start:
                    raise UserError(strWarning)
