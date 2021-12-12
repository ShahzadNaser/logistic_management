# Copyright (c) 2013, Raj Tailot and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = get_columns(filters), get_data(filters)
	return columns, data


def get_data(filters):
	data = frappe.db.sql("""select name,customer,posting_date,grand_total from `tabSales Invoice` where docstatus < 2 and customer = %s and posting_date between %s and %s""",(filters.get("customer"),filters.get("from_date"),filters.get("to_date")),as_dict = 1)
	return data

def get_columns(filters):

	columns = [
		{
			"label": _("Date"),
			"fieldname": "posting_date",
			"fieldtype": "Date",
			"width": 100
		},
	
		{
			"label": _("Customer"),
			"fieldname": "customer",
			"fieldtype": "Link",
			"options":"Customer",
			"width": 220
		},
		{
			"label": _("Invoice Id"),
			"fieldname": "name",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": _("Amount"),
			"fieldname": "grand_total",
			"fieldtype": "Float",
			"width": 100
		}
	]

	return columns


