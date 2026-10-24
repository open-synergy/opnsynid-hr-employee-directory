# Deactivate Employment Status

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.employment_status`\
> **Menu:** Human Resource > Configuration > Career > Employment Status\
> **Actor:** user in group _Employment Status_\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The employment status is currently active.
- **Access:** User is in group _Employment Status_.

## Flow

1. Open the **Human Resource > Configuration > Career > Employment Status** menu.
2. Find and open the record to deactivate.
3. Click the **Action** menu, then click **Archive**.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The employment status is archived and no longer appears in the default list.
- It can no longer be selected on new records. Records that already use it can still be
  viewed.
