from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'heatmap': False,
		# 'heatmap_message': _('This is based on the Time Sheets created against this project'),
		'fieldname': 'shipment',
		'transactions': [
			# {
			# 	'label': _('Project'),
			# 	'items': ['Task', 'Expense Claim', 'Issue']
			# },
			
			{
				'label': _('Sales'),
				'items': ['Sales Order']
			},
			# {
			# 	'label': _('Purchase'),
			# 	'items': ['Purchase Order', 'Purchase Invoice']
			# },
			{
				'label': _('Shipment Documents'),
				'items': ['House Bill']
			},
		]
	}
