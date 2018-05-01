# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class citas_madl(models.Model):
#     _name = 'citas_madl.citas_madl'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class cita(models.Model):

	_name = 'citas_madl.cita'
	
	autor = fields.Char(string="Autor", required=True)
	cita = fields.Text(string="Cita", required=True, translate=True)
        fecha = fields.Date(string="Fecha de visualización", required=True)
	orden = fields.Integer(string="Orden de visualización", required=True)
	
