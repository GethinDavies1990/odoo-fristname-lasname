# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields,models,api

class CrmFields(models.Model):
	_inherit = 'crm.lead'

	sh_firstname = fields.Char("Firstname")
	sh_lastname = fields.Char("Lastname")

	@api.onchange('sh_firstname','sh_lastname')
	def on_change_first_last(self):
		if self.sh_lastname:
			self.name = f'{self.sh_firstname} {self.sh_lastname}'
		else:
			self.name = f'{self.sh_firstname}'
