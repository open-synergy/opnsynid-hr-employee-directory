# Edit Job Grade Category

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.job_grade_category`\
> **Menu:** Human Resource > Configuration > Organization > Job Grade Categories\
> **Actor:** user in group _Job Grade Category_\
> **Requires:** `01-create`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Record:** The job grade category exists.
- **Config:** Optional, only to use **Generate Code**: a sequence template is set for
  this model.
- **Access:** User is in group _Job Grade Category_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Grade Categories**
   menu.
2. Find and open the record to edit.
3. Click the **Edit** button.
4. Change the fields as needed, for example **Job Grade Category**, **Code**.
   Optionally, click **Generate Code** to assign a code to a record whose **Code** is
   `/`.
5. Click **Save**.

## Post-Condition

- The record is updated with the new values.
- Saving fails when another record already uses the same **Code**, except for the code
  `/`.
