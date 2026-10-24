/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_hr_employee.hr_employment_status_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/hr_employment_status/01-create.md
    tour.register(
        "ssi_hr_employee_hr_employment_status_create",
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
                content: "Open the Employment Status menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_hr_employee.hr_employment_status_menu"]',
            },
            {
                content: "Employment Status list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Employment Status)",
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
                run: "text TOUR-HR-EMPLOYMENT-STATUS-CREATE",
            },
            {
                content: "Enter the code",
                trigger: ".o_field_widget[name='code']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text /",
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
                content: "The new employment status is shown",
                trigger:
                    ".o_field_widget[name='name']:contains(TOUR-HR-EMPLOYMENT-STATUS-CREATE)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
