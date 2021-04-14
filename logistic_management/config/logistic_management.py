from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
	config = [
		{
			"label": _("Logistic Management"),
			"items": [
				{
					"type": "doctype",
					"name": "Shipment Management",
					"description": _("Manage All Shipment here."),
					"onboard": 1,
				},
				
			]
		},
		

	]

	
	return config
