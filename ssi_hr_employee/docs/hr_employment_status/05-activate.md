# Activate Employment Status

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.employment_status`\
> **Menu:** Human Resource > Configuration > Career > Employment Status\
> **Actor:** user in group _Employment Status_\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The employment status is currently archived.
- **Access:** User is in group _Employment Status_.

## Flow

1. Open the **Human Resource > Configuration > Career > Employment Status** menu.
2. Enable the **Archived** filter in the search bar.
3. Find and open the record to reactivate.
4. Click the **Action** menu, then click **Unarchive**.

## Post-Condition

- The employment status is restored and appears again in the default list.
