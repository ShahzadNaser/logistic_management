# Copyright (c) 2013, Raj Tailot and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = get_columns(filters), get_data(filters)
	return columns, data


# def get_data(filters):
# 	# data = frappe.db.sql("""select si.customer as party,sm.name as job_no,sm.date,si.name as ref_no,si.posting_date, sum(si.base_grand_total) as collected , sum(pi.base_grand_total) as expense ,(si.base_grand_total - pi.base_grand_total) as profit_loss from `tabHouse Bill` hb left join `tabSales Invoice` si on si.house_bill = hb.name left join `tabPurchase Invoice` pi on pi.house_bill = hb.name inner join `tabShipment Job Master` as sm on hb.shipment = sm.name where si.docstatus < 2 and pi.docstatus < 2 and sm.date between %s and %s group by sm.name""",(filters.get("from_date"),filters.get("to_date")), as_dict = 1)

# 	data = frappe.db.sql("""select si.customer as party,sm.name as job_no,sm.date,si.name as ref_no,si.posting_date, sum(si.base_grand_total) as collected , sum(pi.base_grand_total) as expense ,(si.base_grand_total - pi.base_grand_total) as profit_loss from `tabHouse Bill` hb inner join `tabShipment Job Master` as sm on hb.shipment = sm.name left join `tabSales Invoice` si on si.house_bill = hb.name left join `tabPurchase Invoice` pi on pi.house_bill = hb.name where si.docstatus < 2 and pi.docstatus < 2 and sm.date between %s and %s""",(filters.get("from_date"),filters.get("to_date")), as_dict = 1)
	
# 	return data


def get_data(filters):
	# sales_invoice = frappe.db.sql("""SELECT (base_grand_total),customer from `tabSales Invoice` where job_no_c = %s and docstatus < 2 """,("AF0120/05/2021"))
	# frappe.throw(str(sales_invoice))
	data = []
	shipment_masters = frappe.db.sql("select name,date from `tabShipment Job Master` where date between %s and %s",(filters.get("from_date"),filters.get("to_date")),as_dict = 1)

	# all shipment master

	for item in shipment_masters:
		sales_invoice_total,purchase_total  = 0.00,0.00
	
		sales_invoice = frappe.db.sql("""SELECT SUM(base_grand_total),customer from `tabSales Invoice` where job_no_c = %s and docstatus < 2 group by job_no_c""",(item.name))
		
		# frappe.msgprint(str(sales_invoice))
		customer = None
		if sales_invoice:
			sales_invoice_total = float(sales_invoice[0][0])
			customer = sales_invoice[0][1]


		purchase = frappe.db.sql("""SELECT SUM(base_grand_total) from `tabPurchase Invoice` where shipment = %s and docstatus < 2 group by shipment""",(item.name))
		
		
		if purchase:
			purchase_total = float(purchase[0][0])

		data.append([item.name,item.date,customer,sales_invoice_total,purchase_total,sales_invoice_total - purchase_total])
	
	return data


def get_columns(filters):

	columns = [
		{
			"label": _("Job File No"),
			"fieldname": "job_no",
			"fieldtype": "Link",
			"options": "Shipment Job Master",
			"width":140
		},
		
		{
			"label": _("Job Date"),
			"fieldname": "date",
			"fieldtype": "Date",
			"width":100
		},
		{
			"label": _("Party Name"),
			"fieldname": "party",
			"fieldtype": "Data",
			"width":260
		},
		{
			"label": _("Collected"),
			"fieldname": "collected",
			"fieldtype": "Float",
			"width":100
		},
		{
			"label": _("Expense"),
			"fieldname": "expense",
			"fieldtype": "Float",
			"width":100
		},
		{
			"label": _("Profit/Loss"),
			"fieldname": "profit_loss",
			"fieldtype": "Float",
			"width":100
		}
		
	]

	return columns
