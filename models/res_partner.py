# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Partner(models.Model):
    _inherit = 'res.partner'

    neighboor = fields.Char(
    )
    reference = fields.Char(
    )
    phone2 = fields.Char(
    )
    email2 = fields.Char(
    )
