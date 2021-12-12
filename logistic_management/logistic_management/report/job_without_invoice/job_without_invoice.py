# Copyright (c) 2013, Raj Tailot and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = get_columns(filters), get_data(filters)
	return columns, data

def get_data(filters):
	data = frappe.db.sql("""select EXTRACT(MONTH FROM sm.date) as month,EXTRACT(YEAR FROM sm.date) as year,sm.name as job_no,sm.shipment_type as type,sm.job_type,sm.total_weight as weight,sm.total_volume as volume, sm.total_number_of_containers as cnt20,sm.total_number_of_container_40 as cnt40, hb.consignee_c as consignee, hb.name as house_bill from `tabShipment Job Master` as sm inner join `tabHouse Bill` as hb on hb.shipment = sm.name left join `tabSales Invoice` si on si.job_no_c = sm.name where si.job_no_c is null
	""", as_dict = 1)
	return data

def get_columns(filters):

	columns = [
		{
			"label": _("Year"),
			"fieldname": "year",
			"fieldtype": "Data",
			"width": 50
		},
		{
			"label": _("Month"),
			"fieldname": "month",
			"fieldtype": "Data",
			"width": 60
		},
		{
			"label": _("Job File No"),
			"fieldname": "job_no",
			"fieldtype": "Link",
			"options":"Shipment Job Master",
			"width": 130
		},
		{
			"label": _("House Bill"),
			"fieldname": "house_bill",
			"fieldtype": "Link",
			"options":"House Bill",
			"width": 130
		},
		{
			"label": _("Consignee"),
			"fieldname": "consignee",
			"fieldtype": "Link",
			"options":"Customer",
			"width": 130
		},
		{
			"label": _("Type"),
			"fieldname": "type",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": _("Job Type"),
			"fieldname": "job_type",
			"fieldtype": "Data",
			"width": 100
		},
		
		{
			"label": _("Container20"),
			"fieldname": "cnt20",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": _("Container40"),
			"fieldname": "cnt40",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": _("Weight"),
			"fieldname": "weight",
			"fieldtype": "Float",
			"width": 100
		},
		{
			"label": _("Volume"),
			"fieldname": "volume",
			"fieldtype": "Float",
			"width": 100
		},
	]

	return columns
