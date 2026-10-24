# Edit Job Family Grade

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.job_family_grade`\
> **Menu:** Human Resource > Configuration > Organization > Job Family Grades\
> **Actor:** user in group _Job Family Grade_\
> **Requires:** `01-create`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Record:** The job family grade exists.
- **Config:** Optional, only to use **Generate Code**: a sequence template is set for
  this model.
- **Access:** User is in group _Job Family Grade_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Family Grades** menu.
2. Find and open the record to edit.
3. Click the **Edit** button.
4. Change the fields as needed, for example **Job Family Grade**, **Code**. Optionally,
   click **Generate Code** to assign a code to a record whose **Code** is `/`.
5. Click **Save**.

## Post-Condition

- The record is updated with the new values.
- Saving fails when another record already uses the same **Code**, except for the code
  `/`.
