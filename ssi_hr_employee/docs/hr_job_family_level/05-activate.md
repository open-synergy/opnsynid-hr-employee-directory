# Activate Job Family Level

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.job_family_level`\
> **Menu:** Human Resource > Configuration > Organization > Job Family Levels\
> **Actor:** user in group _Job Family Level_\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The job family level is currently archived.
- **Access:** User is in group _Job Family Level_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Family Levels** menu.
2. Enable the **Archived** filter in the search bar.
3. Find and open the record to reactivate.
4. Click the **Action** menu, then click **Unarchive**.

## Post-Condition

- The job family level is restored and appears again in the default list.
