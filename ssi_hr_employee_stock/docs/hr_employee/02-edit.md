# Edit Employee

> **Module:** `ssi_hr_employee_stock`\
> **Extends:** ssi_hr — model `hr.employee`, aksi `02-edit`

## Additional Fields

- Anchor: after Flow step 3 (**Edit** button) of the base instruction, the **Inventory**
  tab can be used in step 4.
  - **Location**: Select the stock location of the employee. It is optional. Use the
    **Create Location** button to create it automatically; see `07-create-location`.
  - **Current Warehouse**: Shows the warehouse of the company of the **Work Address**.
    It is read only and is empty when no warehouse matches.
