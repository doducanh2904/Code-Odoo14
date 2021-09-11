# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class transportation(models.Model):
    _name = 'transportation.manage'
    _description = 'transportation_manage_byDoDucAnh'

    licensePlate = fields.Char('LicensePlate',required=True)
    vehicleType = fields.Text('Vehicle Type')
    dayProduce = fields.Date('Day Produce')
    tonnage = fields.Float('Tonnage',required=False)
    status= fields.Char('status')
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
