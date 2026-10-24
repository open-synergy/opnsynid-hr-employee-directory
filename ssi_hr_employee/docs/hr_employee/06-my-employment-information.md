# Update My Employment Information

> **Module:** `ssi_hr_employee`\
> **Model:** `hr.employee`\
> **Extends:** ssi_hr — model `hr.employee`\
> **Menu:** Human Resource > My Employment Information\
> **Actor:** employee user\
> **Inline Actions:** `action_dummy_save` (Save)

## Pre-Condition

- **Record:** The user is linked to an employee record.
- **Access:** User is an internal user. The menu is not limited to a group.

## Flow

1. Open the **Human Resource > My Employment Information** menu. The form of the
   employee linked to the user opens directly, without a list.
2. Change the contact details as needed:
   - **Work Mobile**, **Work Phone**, **Work Email**: Enter the work contact details.
   - The photo and **Employee's Name** are shown but cannot be changed here.
3. On the **Private Information** tab, change the personal data as needed, for example
   the work permit, marital status, citizenship, and the number of children.
4. On the **Experiences** tab, add or change the academic, certification, and
   professional experience lines. Click **Add a line** to open the line form.
5. On the **Languages** tab, click **Add a line** and enter the language with its
   ratings in the new row. Optionally, open the line to edit it in a form.
6. Click **Save**. This is the **Save** button in the form header; it only stores the
   changes.

## Post-Condition

- The changes are stored on the employee record of the user.
- The **Job Description** tab shows the job descriptions of the job position of the
  employee. It is read only.
