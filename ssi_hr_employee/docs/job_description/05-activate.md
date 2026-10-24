# Activate Job Description

> **Module:** `ssi_hr_employee`\
> **Model:** `job_description`\
> **Menu:** Human Resource > Configuration > Organization > Job Description\
> **Actor:** user in group _Job Description_\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The job description is currently archived.
- **Access:** User is in group _Job Description_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Description** menu.
2. Enable the **Archived** filter in the search bar.
3. Find and open the record to reactivate.
4. Click the **Action** menu, then click **Unarchive**.

## Post-Condition

- The job description is restored and appears again in the default list.
