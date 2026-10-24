# Edit Employee

> **Module:** `ssi_hr_employee`\
> **Extends:** ssi_hr — model `hr.employee`, aksi `02-edit`

## Additional Fields

- Anchor: after Flow step 3 (**Edit** button) of the base instruction, the fields below
  can be changed in step 4. They are optional.
  - **Organization Unit**, **Job Grade**, **Employment Status**, **Legal Address**: see
    `01-create` for what each field does.
  - **Join Date**, **Termination Date**, **Permanent Date**, **Contract Start Date**,
    **Contract End Date**: Change the employment dates. Setting **Termination Date**
    stops the **Work Longevity** count at that date.
- **Job Grade**, **Employment Status**, and the employment dates are on the **HR
  Settings** tab; **Legal Address** is on the **Private Information** tab.
- Changing **Organization Unit** clears **Department**; select **Department** again.

## Modified Validation

- Saving fails when **Contract End Date** is earlier than **Contract Start Date**.
