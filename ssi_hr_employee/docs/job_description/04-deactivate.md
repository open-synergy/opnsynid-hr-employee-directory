# Deactivate Job Description

> **Module:** `ssi_hr_employee`\
> **Model:** `job_description`\
> **Menu:** Human Resource > Configuration > Organization > Job Description\
> **Actor:** user in group _Job Description_\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The job description is currently active.
- **Access:** User is in group _Job Description_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Description** menu.
2. Find and open the record to deactivate.
3. Click the **Action** menu, then click **Archive**.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The job description is archived and no longer appears in the default list.
- It can no longer be selected on new records. Records that already use it can still be
  viewed.
