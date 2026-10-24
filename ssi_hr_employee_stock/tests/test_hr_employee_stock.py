# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHrEmployeeStock(YamlTransactionCase):
    """Cover the stock location actions and warehouse of ``hr.employee``."""

    def test_hr_employee_stock(self):
        """Run the employee location and warehouse YAML scenarios."""
        self.run_yaml_scenario("test_data_hr_employee_stock.yaml")
