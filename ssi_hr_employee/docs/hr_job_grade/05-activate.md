# Activate Job Grade

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.job_grade`\
> **Menu:** Human Resource > Configuration > Organization > Job Grades\
> **Actor:** user in group _Job Grade_\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The job grade is currently archived.
- **Access:** User is in group _Job Grade_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Grades** menu.
2. Enable the **Archived** filter in the search bar.
3. Find and open the record to reactivate.
4. Click the **Action** menu, then click **Unarchive**.

## Post-Condition

- The job grade is restored and appears again in the default list.
