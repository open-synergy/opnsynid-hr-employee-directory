/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_hr_employee_stock.hr_employee_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/hr_employee/07-create-location.md
    // Navigation comes from the base work instruction of ssi_hr.
    tour.register(
        "ssi_hr_employee_stock_hr_employee_create_location",
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
                content: "Open the employee",
                trigger:
                    ".o_data_row:contains(TOUR-EMP-STOCK-CREATE) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Employee form is displayed",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "The Create Location button is displayed",
                trigger:
                    ".o_statusbar_buttons button[name='action_create_employee_location']",
                extra_trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Click the Create Location button",
                trigger:
                    ".o_statusbar_buttons button[name='action_create_employee_location']",
                extra_trigger: ".o_form_view",
            },
            {
                // Only visible once the action has been applied, so it is a
                // real gate for the state change.
                content: "The Delete Location button is displayed",
                trigger:
                    ".o_statusbar_buttons button[name='action_delete_employee_location']",
                extra_trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Click the Inventory tab",
                trigger: ".o_notebook .nav-link:contains(Inventory)",
                extra_trigger: ".o_form_view",
            },
            {
                content: "The new location is shown",
                trigger:
                    ".o_notebook .tab-pane.active .o_field_widget[name='location_id']:contains(TOUR-EMP-STOCK-CREATE)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/hr_employee/08-delete-location.md
    // Navigation comes from the base work instruction of ssi_hr.
    tour.register(
        "ssi_hr_employee_stock_hr_employee_delete_location",
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
                content: "Open the employee",
                trigger:
                    ".o_data_row:contains(TOUR-EMP-STOCK-DELETE) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Employee form is displayed",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "The Delete Location button is displayed",
                trigger:
                    ".o_statusbar_buttons button[name='action_delete_employee_location']",
                extra_trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Click the Delete Location button",
                trigger:
                    ".o_statusbar_buttons button[name='action_delete_employee_location']",
                extra_trigger: ".o_form_view",
            },
            {
                // Only visible once the action has been applied, so it is a
                // real gate for the state change.
                content: "The Create Location button is displayed",
                trigger:
                    ".o_statusbar_buttons button[name='action_create_employee_location']",
                extra_trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
