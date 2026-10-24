# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHrEmployee(YamlTransactionCase):
    """Cover the HR directory models and the employee extension."""

    def test_hr_employee(self):
        """Run the HR employee YAML scenarios."""
        self.run_yaml_scenario("test_data_hr_employee.yaml")

    def test_job_family_level_name_get(self):
        """Assert the display name returned by ``name_get``.

        Pure Python - trigger P1 (L-01: the ``call`` action discards the
        return value, so YAML cannot assert the display name).
        """
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
        level = self.env["hr.job_family_level"].create(
            {
                "name": "Valid Level",
                "code": "VALL",
                "job_family_id": family.id,
                "job_family_grade_id": fam_grade.id,
                "min_job_grade_id": grade_a.id,
                "max_job_grade_id": grade_b.id,
            }
        )
        self.assertEqual(
            level.name_get(),
            [
                [
                    level.id,
                    "Level Grade Test Family Level (Grade A Level - Grade B Level)",
                ]
            ],
        )
