# Create Employee Location

> **Module:** `ssi_hr_employee_stock`\
> **Model:** `hr.employee`\
> **Menu:** Human Resource > Employees\
> **Actor:** user who can open employee records\
> **Extends:** ssi_hr — model `hr.employee`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The employee is saved and its **Location** is empty. The **Create
  Location** button is hidden when a location is already set.
- **Module:** `ssi_hr_employee_stock` is installed.

## Flow

1. Open the **Human Resource > Employees** menu.
2. Find and open the employee.
3. Click the **Create Location** button in the form header.

## Post-Condition

- An internal stock location is created. It is named after the employee and has the
  location type **Employee**.
- The location is set in the **Location** field on the **Inventory** tab.
- The **Create Location** button is hidden and the **Delete Location** button is shown.
