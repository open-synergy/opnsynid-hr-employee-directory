# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HrEmployee(models.Model):
    """
    Extension of hr.employee with stock location integration.

    Adds a dedicated internal stock location per employee and a computed
    field for the current warehouse derived from the employee's work address.
    Provides action methods to create or delete the employee's stock location.
    """

    _inherit = "hr.employee"

    location_id = fields.Many2one(
        string="Location",
        comodel_name="stock.location",
        ondelete="restrict",
    )
    current_warehouse_id = fields.Many2one(
        string="Current Warehouse",
        comodel_name="stock.warehouse",
        compute="_compute_current_warehouse_id",
        store=True,
        compute_sudo=True,
    )

    @api.depends(
        "address_id",
    )
    def _compute_current_warehouse_id(self):
        """Compute the warehouse of the employee work address.

        The warehouse is the first one whose partner is the parent
        company of ``address_id``. It stays empty when ``address_id``
        is not set, has no parent company, or no warehouse matches.
        """
        for record in self:
            result = False
            Warehouse = self.env["stock.warehouse"]  # pylint: disable=invalid-name
            if record.address_id:
                if record.address_id.parent_id:
                    parent = record.address_id.parent_id
                    criteria = [("partner_id", "=", parent.id)]
                    warehouses = Warehouse.search(criteria)
                    if len(warehouses) > 0:
                        result = warehouses[0]
            record.current_warehouse_id = result

    def action_create_employee_location(self):
        """Create the stock location of the employee.

        Run by the **Create Location** button. Each record is processed
        with ``sudo()`` and delegated to ``_create_employee_location``.

        :return: None
        """
        for record in self.sudo():
            record._create_employee_location()

    def action_delete_employee_location(self):
        """Delete the stock location of the employee.

        Run by the **Delete Location** button. Each record is processed
        with ``sudo()`` and delegated to ``_delete_employee_location``.

        :return: None
        """
        for record in self.sudo():
            record._delete_employee_location()

    def _create_employee_location(self):
        """Create an internal stock location named after the employee.

        The location gets the ``Employee`` location type and is stored
        in ``location_id``. It does not check for an existing location.

        :return: None
        """
        self.ensure_one()
        employee_location_type = self.env.ref(
            "ssi_hr_employee_stock.location_type_employee"
        )
        data = {
            "name": self.name,
            "usage": "internal",
            "type_id": employee_location_type.id,
        }
        location = self.env["stock.location"].create(data)
        self.write(
            {
                "location_id": location.id,
            }
        )

    def _delete_employee_location(  # pylint: disable=inconsistent-return-statements
        self,
    ):
        """Unlink and delete the stock location of the employee.

        The reference in ``location_id`` is cleared first, then the
        location is deleted. Nothing happens when ``location_id`` is
        not set.

        :return: ``True`` when there is no location, otherwise None
        """
        self.ensure_one()
        location = self.location_id
        if not location:
            return True

        self.write(
            {
                "location_id": False,
            }
        )
        location.unlink()
