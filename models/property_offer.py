from odoo import models, fields, api
from datetime import timedelta

from odoo.exceptions import ValidationError


class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Offer"

    name = fields.Char(string="Name")
    price = fields.Float(string="Price")
    status = fields.Selection(
        [("accepted", "Accepted"), ("rejected", "Rejected")],
    )

    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate.property", string="Property")

    validity = fields.Integer(string="Validity", inverse="_inverse_deadline")
    deadline = fields.Date(string="Deadline", compute="_compute_deadline")


    @api.model
    def _get_current_date(self):
        return fields.Date.today()


    @api.depends("validity", "creation_date")
    def _compute_deadline(self):
        for rec in self:
            if rec.validity and rec.creation_date:
                rec.deadline = rec.creation_date + timedelta(days=rec.validity)
            else:
                rec.deadline = False

    def _inverse_deadline(self):
        for rec in self:
            if rec.deadline and rec.creation_date:
                rec.validity = (rec.deadline - rec.creation_date).days

    @api._model_create_multi
    def create(self, vals):
        for rec in vals:
            if not rec.get["creation_date"]:
                rec["creation_date"] = fields.Date.to_date()
        return super(PropertyOffer, self).create(vals)

    @api.constrains("validity")
    def _check_validity(self):
        for rec in self:
            if rec.deadline <= rec.creation_date:
                raise ValidationError("Deadline must be greater than creation date")



    creation_date = fields.Date(string="Creation Date", default=_get_current_date)
