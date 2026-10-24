# Deactivate Job Grade

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.job_grade`\
> **Menu:** Human Resource > Configuration > Organization > Job Grades\
> **Actor:** user in group _Job Grade_\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The job grade is currently active.
- **Access:** User is in group _Job Grade_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Grades** menu.
2. Find and open the record to deactivate.
3. Click the **Action** menu, then click **Archive**.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The job grade is archived and no longer appears in the default list.
- It can no longer be selected on new records. Records that already use it can still be
  viewed.
