# Deactivate Employee Competency

> **Module:** `ssi_hr_employee`\
> **Model:** `employee_competency`\
> **Menu:** Human Resource > Configuration > Employee > Competencies\
> **Actor:** user in group _Employee Competency_\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The employee competency is currently active.
- **Access:** User is in group _Employee Competency_.

## Flow

1. Open the **Human Resource > Configuration > Employee > Competencies** menu.
2. Find and open the record to deactivate.
3. Click the **Action** menu, then click **Archive**.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The employee competency is archived and no longer appears in the default list.
- It can no longer be selected on new records. Records that already use it can still be
  viewed.
