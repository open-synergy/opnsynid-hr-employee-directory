/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_hr_employee_operating_unit.hr_employee_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/hr_employee/01-create.md
    // Delta-only: navigation comes from the base work instruction of ssi_hr;
    // only the additional Operating Unit field is exercised.
    tour.register(
        "ssi_hr_employee_operating_unit_hr_employee_create",
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
                content: "Employees list is displayed",
                trigger: ".o_control_panel:not(.oe_tour_stale)",
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
                content: "Enter the employee name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR-EMPLOYEE-OU",
            },
            // -- Additional Fields: Operating Unit is on the main form.
            {
                content: "Select the operating unit",
                trigger: ".o_field_many2one[name='operating_unit_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR-OU-NAME",
            },
            {
                // The dropdown item is the display name of operating.unit,
                // "[code] name", so match the name part.
                content: "Pick the operating unit from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(TOUR-OU-NAME)",
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
                content: "The operating unit is shown",
                trigger:
                    ".o_field_widget[name='operating_unit_id']:contains(TOUR-OU-NAME)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
