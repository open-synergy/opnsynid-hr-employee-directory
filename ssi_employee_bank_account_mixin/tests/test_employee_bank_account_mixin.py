# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestMixinEmployeeBankAccount(YamlTransactionCase):
    def test_mixin_employee_bank_account_in_env(self):
        """Abstract mixin model is registered in the environment."""
        self.assertIn("mixin.employee_bank_account", self.env)

    def test_mixin_inherits_employee_document(self):
        """mixin.employee_bank_account inherits from mixin.employee_document."""
        self.assertIn(
            "mixin.employee_document",
            self.env["mixin.employee_bank_account"]._inherit,
        )

    def test_default_employee_id_no_employee(self):
        """Inherited _default_employee_id returns None when user has no employee."""
        result = self.env["mixin.employee_bank_account"]._default_employee_id()
        self.assertFalse(result)
