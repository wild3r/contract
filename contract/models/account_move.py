# Copyright 2016 Tecnativa - Carlos Dauden
# Copyright 2018 ACSONE SA/NV.
# Copyright 2020 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, fields, models
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = "account.move"

    # We keep this field for migration purpose
    old_contract_id = fields.Many2one("contract.contract")

    def unlink(self):
        if not self.env.user.has_group('contract.group_delete_invoices_contracts'):
            raise ValidationError(_("No puede eliminar un comprobante"))
        return super().unlink()


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    contract_line_id = fields.Many2one(
        "contract.line", string="Contract Line", index=True
    )
