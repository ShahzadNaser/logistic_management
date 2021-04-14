# -*- coding: utf-8 -*-
# Copyright (c) 2021, Raj Tailot and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class ShipmentJobMaster(Document):
	def autoname(self):
		# frappe.msgprint("here")
		self.name = make_autoname('{}.####./.MM./.YYYY.'.format(self.job_type))

	def validate(self):
		self.validate_duplicate_container()
		self.validate_container_number()

	def validate_duplicate_container(self):
		container_list = []
		for item in self.container_details:
			if item.container_number not in container_list:
				container_list.append(item.container_number)
			else:
				frappe.throw("Container {} is repeated".format(item.container_number))

	def validate_container_number(self):
		if self.total_number_of_containers:
			container_20 = 0
			for item in self.container_details:
				# frappe.msgprint(str(item.size))
				if item.size == '20':
					container_20 = container_20 + 1
			# frappe.msgprint(str(container_20))
			# frappe.msgprint(str(self.total_number_of_containers))
			if str(container_20) != str(self.total_number_of_containers):
				frappe.throw("Please Check 20' Container Details in Table")

		if self.total_number_of_container_40:
			container_40 = 0
			for item in self.container_details:
				if item.size == '40':
					container_40 = container_40 + 1
			# frappe.msgprint(str(container_40))
			# frappe.msgprint(str(self.total_number_of_container_40))
			if str(container_40) != str(self.total_number_of_container_40):
				frappe.throw("Please Check 40' Container Details in Table")
