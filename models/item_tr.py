# -*- coding: utf-8 -*-
from odoo import fields, models


class ItemTr(models.Model):
    _name = 'item.tr'
    _description = 'Item Tr'

    production = fields.Char(string='Producción')
