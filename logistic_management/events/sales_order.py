
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe

def validate(doc, method):
    if doc.payment_schedule:
        for payment in doc.payment_schedule:
            if payment.get("payment_amount") <= 0:
                frappe.throw("Payment Amount in Payment Schedule Cannot be Zero.")