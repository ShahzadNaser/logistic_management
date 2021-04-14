from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'heatmap': False,
		# 'heatmap_message': _('This is based on the Time Sheets created against this project'),
		'fieldname': 'house_bill',
		'transactions': [
			{
				'label': _('Project'),
				'items': ['Task', 'Expense Claim', 'Issue']
			},
			{
				'label': _('Sales'),
				'items': ['Sales Invoice']
			},
			{
				'label': _('Purchase'),
				'items': ['Purchase Invoice']
			},
		]
	}
