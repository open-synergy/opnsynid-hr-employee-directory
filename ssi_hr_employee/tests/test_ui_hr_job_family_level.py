# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiJobFamilyLevel(HttpSavepointCase):
    """Tour tests for the ``job family level`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the job family, family grade, and grades picked by the tour."""
        super().setUpClass()
        obj_grade = cls.env["hr.job_grade"]
        cls.grade_a = obj_grade.create(
            {"name": "TOUR-LVL-GRADE-A", "code": "/", "sequence": 1000}
        )
        cls.grade_b = obj_grade.create(
            {"name": "TOUR-LVL-GRADE-B", "code": "/", "sequence": 1001}
        )
        cls.family_grade = cls.env["hr.job_family_grade"].create(
            {"name": "TOUR-LVL-FGRADE", "code": "/"}
        )
        cls.family = cls.env["hr.job_family"].create(
            {
                "name": "TOUR-LVL-FAMILY",
                "code": "/",
                "min_job_grade_id": cls.grade_a.id,
                "max_job_grade_id": cls.grade_b.id,
            }
        )

    def test_create(self):
        """Run the create tour for ``job family level``.

        IK: docs/hr_job_family_level/01-create.md
        """
        self.start_tour(
            "/web", "ssi_hr_employee_hr_job_family_level_create", login="admin"
        )
