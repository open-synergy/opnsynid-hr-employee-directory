# Activate Job Family

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.job_family`\
> **Menu:** Human Resource > Configuration > Organization > Job Families\
> **Actor:** user in group _Job Family_\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The job family is currently archived.
- **Access:** User is in group _Job Family_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Families** menu.
2. Enable the **Archived** filter in the search bar.
3. Find and open the record to reactivate.
4. Click the **Action** menu, then click **Unarchive**.

## Post-Condition

- The job family is restored and appears again in the default list.
