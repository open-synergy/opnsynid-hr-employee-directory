# Activate Employee Skill

> **Module:** `ssi_hr_employee`\
> **Model:** `employee_skill`\
> **Menu:** Human Resource > Configuration > Employee > Skills\
> **Actor:** user in group _Employee Skill_\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The employee skill is currently archived.
- **Access:** User is in group _Employee Skill_.

## Flow

1. Open the **Human Resource > Configuration > Employee > Skills** menu.
2. Enable the **Archived** filter in the search bar.
3. Find and open the record to reactivate.
4. Click the **Action** menu, then click **Unarchive**.

## Post-Condition

- The employee skill is restored and appears again in the default list.
