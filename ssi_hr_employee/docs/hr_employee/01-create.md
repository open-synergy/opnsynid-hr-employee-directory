# Create Employee

> **Module:** `ssi_hr_employee`\
> **Extends:** ssi_hr — model `hr.employee`, aksi `01-create`

## Additional Fields

When this module is installed, the employee form gains the following fields. All of them
are optional.

- **Organization Unit**: Select the organization unit (a department) of the employee. It
  is on the main part of the form, before **Department**. Once selected, **Department**
  is cleared and can only be chosen from the organization unit and its child
  departments.
- On the **HR Settings** tab, next to **Job Position**:
  - **Job Grade**: Select the job grade of the employee. Only the job grades of the
    selected **Job Position** can be chosen, so select **Job Position** first.
  - **Employment Status**: Select the employment status of the employee.
  - **Join Date**, **Termination Date**, **Permanent Date**, **Contract Start Date**,
    **Contract End Date**: Enter the employment dates of the employee. **Contract End
    Date** must not be earlier than **Contract Start Date**.
- On the **Private Information** tab:
  - **Legal Address**: Select the contact that holds the legal address of the employee.
    The street, city, state, ZIP, country, and phone of that contact are shown on the
    form and cannot be edited there.
- **Job Description** tab: Shows the job descriptions of the selected **Job Position**.
  It is read only.

## Modified Validation

- Saving fails when **Contract End Date** is earlier than **Contract Start Date**.

## Additional Post-Condition

- **Work Longevity** is shown in years and months, calculated from **Join Date** until
  **Termination Date**, or until today when the employee is not terminated. It is zero
  when **Join Date** is empty.
