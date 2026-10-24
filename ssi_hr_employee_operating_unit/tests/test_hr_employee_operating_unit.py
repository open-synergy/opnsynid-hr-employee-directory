# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHrEmployeeOperatingUnit(YamlTransactionCase):
    """Test the operating unit scoping of ``hr.employee``."""

    def test_hr_employee_operating_unit(self):
        """Run the operating unit assignment and visibility scenarios.

        Covers the ``operating_unit_id`` field and the global record rule
        ``hr_employee_rule_ou`` that hides employees of other operating
        units.
        """
        self.run_yaml_scenario("test_data_hr_employee_operating_unit.yaml")
