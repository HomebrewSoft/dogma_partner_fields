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
    category_parent_ids = fields.Many2many(
        related='parent_id.category_id',
        string=_('Etiquetas de la Cia.'),
    )
    phone_direct = fields.Char(
        string=_('Direct'),
    )
    phone_direct_ext = fields.Char(
        string=_('Ext.'),
        size=5,
    )
