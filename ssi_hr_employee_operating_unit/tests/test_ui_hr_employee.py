# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHrEmployee(HttpSavepointCase):
    """Tour tests for the ``hr.employee`` operating unit work instruction."""

    @classmethod
    def setUpClass(cls):
        """Create the operating unit picked by the tour."""
        super().setUpClass()
        cls.operating_unit = cls.env["operating.unit"].create(
            {
                "name": "TOUR-OU-NAME",
                "code": "TOUROU",
                "partner_id": cls.env.company.partner_id.id,
            }
        )

    def test_create(self):
        """Run the create tour for the ``hr.employee`` extension.

        IK: docs/hr_employee/01-create.md
        """
        self.start_tour(
            "/web", "ssi_hr_employee_operating_unit_hr_employee_create", login="admin"
        )
