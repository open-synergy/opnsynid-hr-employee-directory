# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestMixinEmployeeDocument(YamlTransactionCase):
    """Cover the registration and defaults of ``mixin.employee_document``.

    The mixin is abstract and has no concrete model, so every check
    here is written in pure Python.
    """

    def test_mixin_employee_document_in_env(self):
        """Abstract mixin model is registered in the environment.

        Pure Python - trigger P1 (L-02: the YAML assert reads a record
        attribute, but registry membership is not a record attribute).
        """
        self.assertIn("mixin.employee_document", self.env)

    def test_default_employee_id_no_employee(self):
        """Default returns a falsy value without a linked employee.

        Pure Python - trigger P1 (L-01: the ``call`` action discards
        the return value of ``_default_employee_id``).
        """
        result = self.env["mixin.employee_document"]._default_employee_id()
        self.assertFalse(result)

    def test_default_employee_id_with_employee(self):
        """Default returns the employee id of the linked employee.

        Pure Python - trigger P1 (L-01: the ``call`` action discards
        the return value of ``_default_employee_id``).
        """
        employee = self.env["hr.employee"].create(
            {"name": "Linked Employee", "user_id": self.env.user.id}
        )
        result = self.env["mixin.employee_document"]._default_employee_id()
        self.assertEqual(result, employee.id)
