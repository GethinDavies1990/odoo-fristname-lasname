# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields,models,api

class ContactField(models.Model):
	_inherit = 'res.partner'

	sh_firstname = fields.Char("Firstname")
	sh_lastname = fields.Char("Lastname")

	@api.onchange('sh_firstname','sh_lastname')
	def on_change_first_last(self):
		name = ''
		if self.sh_firstname:
			name = self.sh_firstname
		if self.sh_lastname:
			if name:
				name += f' {self.sh_lastname}'
			else:
				name = self.sh_lastname
		self.name = name
