# Activate Job Family Grade

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.job_family_grade`\
> **Menu:** Human Resource > Configuration > Organization > Job Family Grades\
> **Actor:** user in group _Job Family Grade_\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The job family grade is currently archived.
- **Access:** User is in group _Job Family Grade_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Family Grades** menu.
2. Enable the **Archived** filter in the search bar.
3. Find and open the record to reactivate.
4. Click the **Action** menu, then click **Unarchive**.

## Post-Condition

- The job family grade is restored and appears again in the default list.
