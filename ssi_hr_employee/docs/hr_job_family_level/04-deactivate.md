# Deactivate Job Family Level

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.job_family_level`\
> **Menu:** Human Resource > Configuration > Organization > Job Family Levels\
> **Actor:** user in group _Job Family Level_\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The job family level is currently active.
- **Access:** User is in group _Job Family Level_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Family Levels** menu.
2. Find and open the record to deactivate.
3. Click the **Action** menu, then click **Archive**.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The job family level is archived and no longer appears in the default list.
- It can no longer be selected on new records. Records that already use it can still be
  viewed.
