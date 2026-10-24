# Deactivate Employee Skill

> **Module:** `ssi_hr_employee`\
> **Model:** `employee_skill`\
> **Menu:** Human Resource > Configuration > Employee > Skills\
> **Actor:** user in group _Employee Skill_\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The employee skill is currently active.
- **Access:** User is in group _Employee Skill_.

## Flow

1. Open the **Human Resource > Configuration > Employee > Skills** menu.
2. Find and open the record to deactivate.
3. Click the **Action** menu, then click **Archive**.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The employee skill is archived and no longer appears in the default list.
- It can no longer be selected on new records. Records that already use it can still be
  viewed.
