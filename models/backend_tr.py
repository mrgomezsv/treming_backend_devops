# -*- coding: utf-8 -*-
from odoo import fields, models


class BackendTr(models.Model):
    _name = 'backend.tr'
    _description = 'Modelo para información de backend'

    ip = fields.Char(string='IP')
    cliente = fields.Char(string='Cliente')
    plataforma = fields.Char(string='Plataforma')
    dominio = fields.Char(string='Dominio')

    production = fields.Many2one('backend.category.tr', string='Produccion')
