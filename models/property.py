from odoo import models, fields, api


class Property(models.Model):
    _name = "estate.property"
    _description = "Property"

    type_id = fields.Many2one('estate.property.type', string='Type')
    tag_ids = fields.Many2many("estate.property.tag", string='Tags')
    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description")
    postcode = fields.Char(string="Postcode")
    date_available = fields.Date(string="Available Date")
    expected_price = fields.Float(string="Expected Price")
    best_offer = fields.Float(string="Best Offer")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bed Rooms")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Face Des")
    garages = fields.Boolean(string="Garages", default=False)
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([("north", "North"), ("east", "East"), ("west", "West"), ("south", "South")],
                                          string="Garden Orientation", default="north")

    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    sale_id = fields.Many2one("res.users", string="Sale man")
    buyer_id = fields.Many2one("res.users", string="Buyer", domain=[("is_company", "=", True)])

    phone = fields.Char(string="Phone", related="buyer_id.phone")
    @api.onchange("living_area", "garden_area")
    def compute_total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area

    total_area = fields.Integer(string="Total Area", compute=compute_total_area)


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"
    name = fields.Char(string="Name")


class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property Tag"
    name = fields.Char(string="Name")
