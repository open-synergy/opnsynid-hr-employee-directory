# Create Employment Status

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.employment_status`\
> **Menu:** Human Resource > Configuration > Career > Employment Status\
> **Actor:** user in group _Employment Status_\
> **Active:** `—` → `true`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Config:** Optional, only to use **Generate Code**: a sequence template is set for
  this model.
- **Access:** User is in group _Employment Status_.

## Flow

1. Open the **Human Resource > Configuration > Career > Employment Status** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Employment Status** _(required)_: Enter the name of the employment status.
   - **Code** _(required)_: Enter a unique code. Enter `/` if no unique code is needed.
4. Optionally, click **Generate Code** to assign a code from the sequence template. Only
   a record whose **Code** is `/` receives a new code.
5. Optionally, enter a remark on the **Note** tab.
6. Click **Save**.

## Post-Condition

- A new employment status is created, is active, and is listed in the Employment Status
  menu.
