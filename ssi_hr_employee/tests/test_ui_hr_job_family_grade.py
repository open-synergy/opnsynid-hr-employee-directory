# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiJobFamilyGrade(HttpSavepointCase):
    """Tour tests for the ``job family grade`` work instructions."""

    def test_create(self):
        """Run the create tour for ``job family grade``.

        IK: docs/hr_job_family_grade/01-create.md
        """
        self.start_tour(
            "/web", "ssi_hr_employee_hr_job_family_grade_create", login="admin"
        )
