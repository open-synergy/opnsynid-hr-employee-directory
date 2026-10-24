# Delete Employee Location

> **Module:** `ssi_hr_employee_stock`\
> **Model:** `hr.employee`\
> **Menu:** Human Resource > Employees\
> **Actor:** user who can open employee records\
> **Extends:** ssi_hr — model `hr.employee`\
> **Requires:** `07-create-location`

## Pre-Condition

- **Record:** The employee is saved and has a **Location**. The **Delete Location**
  button is hidden when the **Location** is empty.
- **Module:** `ssi_hr_employee_stock` is installed.

## Flow

1. Open the **Human Resource > Employees** menu.
2. Find and open the employee.
3. Click the **Delete Location** button in the form header.

## Post-Condition

- The **Location** field of the employee is cleared and the stock location is deleted.
- The **Delete Location** button is hidden and the **Create Location** button is shown.
- The deletion is refused if the stock location is still referenced by other records,
  for example by stock moves.
