# Create Job Position

> **Module:** `ssi_hr_employee`\
> **Extends:** ssi_hr — model `hr.job`, aksi `01-create`

## Additional Fields

When this module is installed, the job position form gains the following fields. All of
them are optional.

- On the **Recruitment** tab, before **Department**:
  - **Job Family Level**: Select the job family level of the position. Selecting or
    clearing it resets **Job Grades**.
  - **Job Grades**: Select one or more job grades of the position. Only the job grades
    of the selected **Job Family Level** can be chosen, so select **Job Family Level**
    first.
- **Job Description** tab: An additional tab where the job descriptions of the position
  are selected. It is shown next to the existing **Job Description** tab.

## Additional Post-Condition

- The job position list also shows the **Job Family Level** column.
- Employees of this position can only be given a **Job Grade** from the **Job Grades**
  selected here.
