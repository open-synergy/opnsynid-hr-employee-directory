# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHrEmployee(HttpSavepointCase):
    """Tour tests for the ``hr.employee`` extension work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the organization unit and status picked by the tour."""
        super().setUpClass()
        cls.org_unit = cls.env["hr.department"].create({"name": "TOUR-ORG-UNIT"})
        cls.status = cls.env["hr.employment_status"].create(
            {"name": "TOUR-EMP-STATUS", "code": "/"}
        )

    def test_create(self):
        """Run the create tour for the ``hr.employee`` extension.

        IK: docs/hr_employee/01-create.md
        """
        self.start_tour("/web", "ssi_hr_employee_hr_employee_create", login="admin")
