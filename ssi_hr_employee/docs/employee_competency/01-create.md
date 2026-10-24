# Create Employee Competency

> **Module:** `ssi_hr_employee`\
> **Model:** `employee_competency`\
> **Menu:** Human Resource > Configuration > Employee > Competencies\
> **Actor:** user in group _Employee Competency_\
> **Active:** `—` → `true`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Config:** Optional, only to use **Generate Code**: a sequence template is set for
  this model.
- **Access:** User is in group _Employee Competency_.

## Flow

1. Open the **Human Resource > Configuration > Employee > Competencies** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name** _(required)_: Enter the name of the employee competency.
   - **Code** _(required)_: Enter a unique code. Enter `/` if no unique code is needed.
4. Optionally, click **Generate Code** to assign a code from the sequence template. Only
   a record whose **Code** is `/` receives a new code.
5. Optionally, enter a remark on the **Note** tab.
6. Click **Save**.

## Post-Condition

- A new employee competency is created, is active, and is listed in the Competencies
  menu.
