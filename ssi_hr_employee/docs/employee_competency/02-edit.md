# Edit Employee Competency

> **Module:** `ssi_hr_employee`\
> **Model:** `employee_competency`\
> **Menu:** Human Resource > Configuration > Employee > Competencies\
> **Actor:** user in group _Employee Competency_\
> **Requires:** `01-create`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Record:** The employee competency exists.
- **Config:** Optional, only to use **Generate Code**: a sequence template is set for
  this model.
- **Access:** User is in group _Employee Competency_.

## Flow

1. Open the **Human Resource > Configuration > Employee > Competencies** menu.
2. Find and open the record to edit.
3. Click the **Edit** button.
4. Change the fields as needed, for example **Name**, **Code**. Optionally, click
   **Generate Code** to assign a code to a record whose **Code** is `/`.
5. Click **Save**.

## Post-Condition

- The record is updated with the new values.
- Saving fails when another record already uses the same **Code**, except for the code
  `/`.
