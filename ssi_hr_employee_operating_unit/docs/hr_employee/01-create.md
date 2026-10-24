# Create Employee

> **Module:** `ssi_hr_employee_operating_unit`\
> **Extends:** ssi_hr — model `hr.employee`, aksi `01-create`

## Additional Pre-Condition

- **Access:** To see the **Operating Unit** field, the user belongs to the group
  **Multiple Operating Unit**. Without it the field is hidden.
- **Record:** At least one operating unit exists and the user is allowed to use it.

## Additional Fields

When this module is installed, the employee form gains one field:

- **Operating Unit**: Select the operating unit of the employee. It is on the main part
  of the form, right after **Organization Unit**. It is optional and defaults to the
  default operating unit of the user. It is shown only to users of the group **Multiple
  Operating Unit**.

## Modified — Record Visibility

- A user only sees the employees of the operating units the user is allowed to use. The
  employees without an operating unit and the employee record of the user are always
  visible. This is not a Flow step.
