# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHrJob(HttpSavepointCase):
    """Tour tests for the ``hr.job`` extension work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the job family level picked by the tour."""
        super().setUpClass()
        obj_grade = cls.env["hr.job_grade"]
        grade_a = obj_grade.create(
            {"name": "TOUR-JOB-GRADE-A", "code": "/", "sequence": 1000}
        )
        grade_b = obj_grade.create(
            {"name": "TOUR-JOB-GRADE-B", "code": "/", "sequence": 1001}
        )
        family_grade = cls.env["hr.job_family_grade"].create(
            {"name": "TOUR-JOB-FGRADE", "code": "/"}
        )
        family = cls.env["hr.job_family"].create(
            {
                "name": "TOUR-JOB-FAMILY",
                "code": "/",
                "min_job_grade_id": grade_a.id,
                "max_job_grade_id": grade_b.id,
            }
        )
        cls.level = cls.env["hr.job_family_level"].create(
            {
                "name": "TOUR-JOB-LEVEL",
                "code": "/",
                "job_family_grade_id": family_grade.id,
                "job_family_id": family.id,
                "min_job_grade_id": grade_a.id,
                "max_job_grade_id": grade_b.id,
            }
        )

    def test_create(self):
        """Run the create tour for the ``hr.job`` extension.

        IK: docs/hr_job/01-create.md
        """
        self.start_tour("/web", "ssi_hr_employee_hr_job_create", login="admin")
