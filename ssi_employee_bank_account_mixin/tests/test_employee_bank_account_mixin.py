# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestMixinEmployeeBankAccount(YamlTransactionCase):
    """Cover the registration of ``mixin.employee_bank_account``.

    The mixin is abstract and has no concrete model, so every check
    here is written in pure Python.
    """

    def test_mixin_employee_bank_account_in_env(self):
        """Abstract mixin model is registered in the environment.

        Pure Python - trigger P1 (L-02: the YAML assert reads a record
        attribute, but registry membership is not a record attribute).
        """
        self.assertIn("mixin.employee_bank_account", self.env)

    def test_mixin_inherits_employee_document(self):
        """Mixin inherits from ``mixin.employee_document``.

        Pure Python - trigger P1 (L-02: the YAML assert reads a record
        attribute, but ``_inherit`` is a class attribute).
        """
        self.assertIn(
            "mixin.employee_document",
            self.env["mixin.employee_bank_account"]._inherit,
        )

    def test_default_employee_id_no_employee(self):
        """Inherited default returns a falsy value without employee.

        Pure Python - trigger P1 (L-01: the ``call`` action discards
        the return value of ``_default_employee_id``).
        """
        result = self.env["mixin.employee_bank_account"]._default_employee_id()
        self.assertFalse(result)
