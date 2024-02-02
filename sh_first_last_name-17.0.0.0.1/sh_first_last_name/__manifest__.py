# Part of Softhealer Technologies.
{
    "name": "FirstName - LastName",
    "author": "Softhealer Technologies",
    "license": "OPL-1",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "version": "0.0.1",
    "category": "Extra Tools",
    "summary": "Partner first name Partner last name Partner first & last name Partner first name & last name Separate Last name Separate First name Employee first name Employee Last Name First Last Name first and last name first name and last name Odoo",
    "description": """This module only for add first name and last name.""",
    "depends": ['base','contacts','crm'],
    "data": [
        'views/res_partner_views.xml',
        'views/crm_leads_views.xml',
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "images": ["static/description/background.png"],
    "price": "5",
    "currency": "EUR"
}
