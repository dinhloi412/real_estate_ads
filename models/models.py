# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class real_estate_ads(models.Model):
#     _name = 'real_estate_ads.real_estate_ads'
#     _description = 'real_estate_ads.real_estate_ads'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
