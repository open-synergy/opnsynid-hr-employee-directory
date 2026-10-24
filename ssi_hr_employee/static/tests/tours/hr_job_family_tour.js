/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_hr_employee.hr_job_family_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/hr_job_family/01-create.md
    tour.register(
        "ssi_hr_employee_hr_job_family_create",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Human Resource app",
                trigger: '.o_app[data-menu-xmlid="ssi_hr.menu_root_human_resource"]',
            },
            {
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_hr.menu_human_resource_configuration"]',
            },
            {
                content: "Open the Job Families menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_hr_employee.hr_job_family_menu"]',
            },
            {
                content: "Job Families list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Job Families)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
            // -- Click the New button.
            {
                content: "Click Create",
                trigger: ".o_list_button_add",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only.
                },
            },
            // -- Fill in the required fields.
            {
                content: "Enter the name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR-HR-JOB-FAMILY-CREATE",
            },
            {
                content: "Enter the code",
                trigger: ".o_field_widget[name='code']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text /",
            },
            {
                content: "Select the minimum grade",
                trigger: ".o_field_many2one[name='min_job_grade_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR-FAM-GRADE-A",
            },
            {
                content: "Pick the minimum grade from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(TOUR-FAM-GRADE-A)",
            },
            {
                content: "Select the maximum grade",
                trigger: ".o_field_many2one[name='max_job_grade_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR-FAM-GRADE-B",
            },
            {
                content: "Pick the maximum grade from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(TOUR-FAM-GRADE-B)",
            },
            // -- Click Save.
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "The new job family is shown",
                trigger:
                    ".o_field_widget[name='name']:contains(TOUR-HR-JOB-FAMILY-CREATE)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
