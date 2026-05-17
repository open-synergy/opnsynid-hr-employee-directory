# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestMixinEmployeeDocument(YamlTransactionCase):
    def test_mixin_employee_document_in_env(self):
        """Abstract mixin model is registered in the environment."""
        self.assertIn("mixin.employee_document", self.env)

    def test_default_employee_id_no_employee(self):
        """_default_employee_id returns None when user has no linked employee."""
        result = self.env["mixin.employee_document"]._default_employee_id()
        self.assertFalse(result)

    def test_default_employee_id_with_employee(self):
        """_default_employee_id returns employee id when user has a linked employee."""
        employee = self.env["hr.employee"].create(
            {"name": "Linked Employee", "user_id": self.env.user.id}
        )
        result = self.env["mixin.employee_document"]._default_employee_id()
        self.assertEqual(result, employee.id)
