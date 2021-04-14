# -*- coding: utf-8 -*-
# Copyright (c) 2021, Raj Tailot and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class HouseBill(Document):

	def after_insert(self):
		# frappe.msgprint("here")
		self.calculate_master_totals(self.shipment,self.shipment_channel)

	def validate(self):
		
		if self.shipment_channel == "Air":
			# frappe.msgprint("Air")
			volume,actual,chargable,qty = 0,0,0,0
			for item in self.cargo_details:
				if item.volume:
					volume = volume + item.volume
				if item.weight:
					actual = actual + item.weight
				if item.chargable_weight:
					chargable = chargable + item.chargable_weight
				if item.quantity:
					qty = qty + item.quantity
			self.total_actual_weight = actual
			self.total_volume = volume
			self.total_chargeable_weight = chargable
			self.total_qty = qty
			# frappe.msgprint(str(qty))
			self.calculate_master_totals(self.shipment,self.shipment_channel)
		
		if self.shipment_channel in ["Land","Sea"]:
			# frappe.msgprint("Air")
			volume,actual,chargable,qty = 0,0,0,0
			for item in self.cargo_details:
				if item.volume:
					volume = volume + item.volume
				if item.weight:
					actual = actual + item.weight
				
				if item.quantity:
					qty = qty + item.quantity
			self.total_actual_weight = actual
			self.total_volume = volume
			self.total_chargeable_weight = chargable
			self.total_qty = qty
			# frappe.msgprint(str(qty))
			self.calculate_master_totals(self.shipment,self.shipment_channel)

			


		if self.shipment_channel in ["Land","Courier"]:
			# frappe.msgprint("LC")
			volume,actual = 0,0
			for item in self.cargo_details:
				volume = volume + item.volume
				actual = actual + item.weight
				
			self.total_actual_weight = actual
			self.total_volume = volume

			self.calculate_master_totals(self.shipment,self.shipment_channel)
			
			

		if self.shipment_channel == "Sea":
			# frappe.msgprint("sea")
			volume,actual = 0,0
			for item in self.sea_cargo_details:
				volume = volume + item.volume
				actual = actual + item.weight
				
			self.total_actual_weight = actual
			self.total_volume = volume

			self.calculate_master_totals(self.shipment,self.shipment_channel)
			

	def calculate_master_totals(self,shimpent_name,type):
		
		value = frappe.db.sql(""" select count(sm.name),sum(sm.total_volume) as total_volume,sum(sm.total_actual_weight) as total_weight,sum(sm.total_chargeable_weight) as total_chargable_weight from `tabHouse Bill` sm where sm.shipment = %s group by sm.shipment """,(shimpent_name), as_dict = 1)
		# frappe.msgprint(str(value))
		if value:
			frappe.db.set_value("Shipment Job Master",shimpent_name,"total_volume",value[0]['total_volume'])
			frappe.db.set_value("Shipment Job Master",shimpent_name,"total_weight",value[0]['total_weight'])
			if type == "Air":
				frappe.db.set_value("Shipment Job Master",shimpent_name,"total_chargeable_weight_kg",value[0]['total_chargable_weight'])

		
		


@frappe.whitelist()
def get_container_filter(doctype, txt, searchfield, start, page_len, filters):
	container_list = frappe.db.sql(""" select cd.container_number from `tabContainer Details` cd where cd.parent = %s""",(filters.get("container")))
	return container_list