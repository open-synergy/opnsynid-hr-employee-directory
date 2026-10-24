/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_hr_employee.hr_job_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/hr_job/01-create.md
    // Delta-only: navigation comes from the base work instruction of ssi_hr;
    // only the additional fields are exercised.
    tour.register(
        "ssi_hr_employee_hr_job_create",
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
                content: "Open the Job Positions menu",
                trigger: '.o_menu_sections [data-menu-xmlid="ssi_hr.hr_job_menu"]',
            },
            {
                content: "Job Positions list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Job Positions)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
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
            {
                content: "Enter the job position name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR-JOB-DELTA",
            },
            // -- Additional Fields: Job Family Level and Job Grades.
            {
                content: "Click the Recruitment tab",
                trigger: ".o_notebook .nav-link:contains(Recruitment)",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Job Grades field is displayed",
                trigger:
                    ".o_notebook .tab-pane.active .o_field_widget[name='job_grade_ids']",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Select the job family level",
                trigger: ".o_field_many2one[name='job_family_level_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR-JOB-LEVEL",
            },
            {
                content: "Pick the job family level from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(TOUR-JOB-FGRADE TOUR-JOB-FAMILY)",
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
                content: "The job family level is shown",
                trigger:
                    ".o_field_widget[name='job_family_level_id']:contains(TOUR-JOB-FGRADE)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
