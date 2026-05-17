# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHrEmployeeStock(YamlTransactionCase):
    def test_hr_employee_stock(self):
        self.run_yaml_scenario("test_data_hr_employee_stock.yaml")

    def test_delete_employee_location_when_none(self):
        """_delete_employee_location returns early when location_id not set."""
        employee = self.env["hr.employee"].create({"name": "Employee No Location"})
        self.assertFalse(employee.location_id)
        # Should not raise - returns True early
        employee.action_delete_employee_location()
        self.assertFalse(employee.location_id)
