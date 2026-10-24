# Create Job Family Level

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.job_family_level`\
> **Menu:** Human Resource > Configuration > Organization > Job Family Levels\
> **Actor:** user in group _Job Family Level_\
> **Active:** `—` → `true`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Data:** The job family grade, the job family, and the job grades already exist. The
  job family has a grade range that covers the grades used here.
- **Config:** Optional, only to use **Generate Code**: a sequence template is set for
  this model.
- **Access:** User is in group _Job Family Level_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Family Levels** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Job Family Grade** _(required)_: Select the job family grade of the level.
   - **Code** _(required)_: Enter a unique code. Enter `/` if no unique code is needed.
   - **Job Family** _(required)_: Select the job family of the level.
   - **Min. Grade** _(required)_: Select the lowest job grade of the level. Only the
     grades of the selected job family can be chosen.
   - **Max. Grade** _(required)_: Select the highest job grade of the level. Only the
     grades of the selected job family can be chosen.
4. Optionally, click **Generate Code** to assign a code from the sequence template. Only
   a record whose **Code** is `/` receives a new code.
5. Optionally, enter a remark on the **Note** tab.
6. Click **Save**.

## Post-Condition

- A new job family level is created, is active, and is listed in the Job Family Levels
  menu.
