# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "HR Employee + Operating Unit",
    "version": "14.0.1.1.1",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_hr_employee",
        "ssi_operating_unit_mixin",
    ],
    "data": [
        "security/ir_rule/ir_rule_data.xml",
        "views/hr_employee_views.xml",
    ],
}
