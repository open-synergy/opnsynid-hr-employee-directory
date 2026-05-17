# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.exceptions import UserError
from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHrEmployee(YamlTransactionCase):
    def test_hr_employee(self):
        self.run_yaml_scenario("test_data_hr_employee.yaml")

    def test_constraint_job_family_min_max_grade(self):
        """Job family min grade must have lower sequence than max grade."""
        grade_a = self.env["hr.job_grade"].create(
            {"name": "Grade A Constraint", "code": "GAC", "sequence": 10}
        )
        grade_b = self.env["hr.job_grade"].create(
            {"name": "Grade B Constraint", "code": "GBC", "sequence": 20}
        )
        with self.assertRaises(UserError):
            self.env["hr.job_family"].create(
                {
                    "name": "Invalid Family",
                    "code": "INVF",
                    "min_job_grade_id": grade_b.id,
                    "max_job_grade_id": grade_a.id,
                }
            )

    def test_constraint_job_family_level_min_max_grade(self):
        """Job family level min grade must have lower sequence than max grade."""
        grade_a = self.env["hr.job_grade"].create(
            {"name": "Grade A Level", "code": "GALVL", "sequence": 10}
        )
        grade_b = self.env["hr.job_grade"].create(
            {"name": "Grade B Level", "code": "GBLVL", "sequence": 20}
        )
        fam_grade = self.env["hr.job_family_grade"].create(
            {"name": "Level Grade", "code": "LVLG"}
        )
        family = self.env["hr.job_family"].create(
            {
                "name": "Test Family Level",
                "code": "TFAMLVL",
                "min_job_grade_id": grade_a.id,
                "max_job_grade_id": grade_b.id,
            }
        )
        with self.assertRaises(UserError):
            self.env["hr.job_family_level"].create(
                {
                    "name": "Invalid Level",
                    "code": "INVL",
                    "job_family_id": family.id,
                    "job_family_grade_id": fam_grade.id,
                    "min_job_grade_id": grade_b.id,
                    "max_job_grade_id": grade_a.id,
                }
            )

    def test_employee_contract_date_constraint(self):
        """Contract end date must be greater than contract start date."""
        from datetime import date as _date

        employee = (
            self.env["hr.employee"].sudo().create({"name": "Test Contract Employee"})
        )
        with self.assertRaises(UserError):
            employee.sudo().write(
                {
                    "date_contract_start": _date(2024, 12, 31),
                    "date_contract_end": _date(2024, 1, 1),
                }
            )
