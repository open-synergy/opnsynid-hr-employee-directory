# Create Job Family

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.job_family`\
> **Menu:** Human Resource > Configuration > Organization > Job Families\
> **Actor:** user in group _Job Family_\
> **Active:** `—` → `true`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Data:** At least two job grades already exist; the minimum grade must not come after
  the maximum grade in the grade order.
- **Config:** Optional, only to use **Generate Code**: a sequence template is set for
  this model.
- **Access:** User is in group _Job Family_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Families** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Job Family** _(required)_: Enter the name of the job family.
   - **Code** _(required)_: Enter a unique code. Enter `/` if no unique code is needed.
   - **Min. Grade** _(required)_: Select the lowest job grade of the family.
   - **Max. Grade** _(required)_: Select the highest job grade of the family.
4. Optionally, click **Generate Code** to assign a code from the sequence template. Only
   a record whose **Code** is `/` receives a new code.
5. Optionally, enter a remark on the **Note** tab.
6. Click **Save**.

## Post-Condition

- A new job family is created, is active, and is listed in the Job Families menu.
