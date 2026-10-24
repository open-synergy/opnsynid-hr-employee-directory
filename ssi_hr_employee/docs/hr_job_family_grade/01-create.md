# Create Job Family Grade

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.job_family_grade`\
> **Menu:** Human Resource > Configuration > Organization > Job Family Grades\
> **Actor:** user in group _Job Family Grade_\
> **Active:** `—` → `true`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Config:** Optional, only to use **Generate Code**: a sequence template is set for
  this model.
- **Access:** User is in group _Job Family Grade_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Family Grades** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Job Family Grade** _(required)_: Enter the name of the job family grade.
   - **Code** _(required)_: Enter a unique code. Enter `/` if no unique code is needed.
4. Optionally, click **Generate Code** to assign a code from the sequence template. Only
   a record whose **Code** is `/` receives a new code.
5. Optionally, enter a remark on the **Note** tab.
6. Click **Save**.

## Post-Condition

- A new job family grade is created, is active, and is listed in the Job Family Grades
  menu.
