/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_hr_employee.hr_employee_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/hr_employee/01-create.md
    // Delta-only: navigation comes from the base work instruction of ssi_hr;
    // only the additional fields are exercised.
    tour.register(
        "ssi_hr_employee_hr_employee_create",
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
                content: "Open the Employees menu",
                trigger: '.o_menu_sections [data-menu-xmlid="ssi_hr.hr_employee_menu"]',
                run: function (actions) {
                    // Employees is the landing menu: the click reloads the same
                    // action, so mark the control panel and wait for a fresh one.
                    $(".o_control_panel").addClass("oe_tour_stale");
                    actions.click();
                },
            },
            {
                content: "Employees kanban is displayed",
                trigger: ".o_control_panel:not(.oe_tour_stale)",
                extra_trigger: ".o_kanban_view",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Click Create",
                trigger: ".o-kanban-button-new",
                extra_trigger: ".o_kanban_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Enter the employee name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR-EMPLOYEE-DELTA",
            },
            // -- Additional Fields: Organization Unit is on the main form.
            {
                content: "Select the organization unit",
                trigger: ".o_field_many2one[name='organization_unit_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR-ORG-UNIT",
            },
            {
                content: "Pick the organization unit from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(TOUR-ORG-UNIT)",
            },
            // -- Additional Fields: HR Settings tab.
            {
                content: "Click the HR Settings tab",
                trigger: ".o_notebook .nav-link:contains(HR Settings)",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Job Grade field is displayed",
                trigger:
                    ".o_notebook .tab-pane.active .o_field_widget[name='job_grade_id']",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Join Date field is displayed",
                trigger:
                    ".o_notebook .tab-pane.active .o_field_widget[name='date_join']",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Contract End Date field is displayed",
                trigger:
                    ".o_notebook .tab-pane.active .o_field_widget[name='date_contract_end']",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Select the employment status",
                trigger: ".o_field_many2one[name='employment_status_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR-EMP-STATUS",
            },
            {
                content: "Pick the employment status from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(TOUR-EMP-STATUS)",
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
                content: "The employment status is shown",
                trigger:
                    ".o_field_widget[name='employment_status_id']:contains(TOUR-EMP-STATUS)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
