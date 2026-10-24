# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHrEmployee(HttpSavepointCase):
    """Tour tests for the employee stock location work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the employees opened by the tours.

        One employee has no location (create tour); the other already
        has a location made through the real action (delete tour).
        """
        super().setUpClass()
        Employee = cls.env["hr.employee"]  # pylint: disable=invalid-name
        cls.employee_create = Employee.create({"name": "TOUR-EMP-STOCK-CREATE"})
        cls.employee_delete = Employee.create({"name": "TOUR-EMP-STOCK-DELETE"})
        cls.employee_delete.action_create_employee_location()

    def test_create_location(self):
        """Run the create location tour for ``hr.employee``.

        IK: docs/hr_employee/07-create-location.md
        """
        self.start_tour(
            "/web", "ssi_hr_employee_stock_hr_employee_create_location", login="admin"
        )

    def test_delete_location(self):
        """Run the delete location tour for ``hr.employee``.

        IK: docs/hr_employee/08-delete-location.md
        """
        self.start_tour(
            "/web", "ssi_hr_employee_stock_hr_employee_delete_location", login="admin"
        )
