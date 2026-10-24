# Create Job Grade

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.job_grade`\
> **Menu:** Human Resource > Configuration > Organization > Job Grades\
> **Actor:** user in group _Job Grade_\
> **Active:** `—` → `true`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Data:** Optionally, the job grade category already exists.
- **Config:** Optional, only to use **Generate Code**: a sequence template is set for
  this model.
- **Access:** User is in group _Job Grade_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Grades** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Job Grade** _(required)_: Enter the name of the job grade.
   - **Code** _(required)_: Enter a unique code. Enter `/` if no unique code is needed.
4. Fill in the optional fields as needed:
   - **Job Grade Category**: Select the category of the job grade.
   - **Sequence**: Enter the order of the grade. Grades are ordered by this number; a
     smaller number is a lower grade. The default is 5.
5. Optionally, click **Generate Code** to assign a code from the sequence template. Only
   a record whose **Code** is `/` receives a new code.
6. Optionally, enter a remark on the **Note** tab.
7. Click **Save**.

## Post-Condition

- A new job grade is created, is active, and is listed in the Job Grades menu.
