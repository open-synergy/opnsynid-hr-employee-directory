# Activate Employee Competency

> **Module:** `ssi_hr_employee`\
> **Model:** `employee_competency`\
> **Menu:** Human Resource > Configuration > Employee > Competencies\
> **Actor:** user in group _Employee Competency_\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The employee competency is currently archived.
- **Access:** User is in group _Employee Competency_.

## Flow

1. Open the **Human Resource > Configuration > Employee > Competencies** menu.
2. Enable the **Archived** filter in the search bar.
3. Find and open the record to reactivate.
4. Click the **Action** menu, then click **Unarchive**.

## Post-Condition

- The employee competency is restored and appears again in the default list.
