# Copyright (c) 2025, Sukalyan and contributors
# For license information, please see license.txt

import frappe
def execute(filters=None):
	## Creating the column for the report
	columns = get_columns()

	## Fetching the data based on filters
	data = get_data(filters)
	
	## Creating a chart
	chart = get_chart_data(data)

	## Columns , Data , Message , Chart
	return columns, data , None , chart

def get_columns():
	columns = [
        {"label": "Month", "fieldname": "month", "fieldtype": "Data", "width": 120},
		{"label": "Low Tariff avg cost", "fieldname": "low_tariff_amount", "fieldtype": "Float", "width": 200},
		{"label": "High Tariff avg cost", "fieldname": "high_tariff_amount", "fieldtype": "Float", "width": 200},
		{"label": "Total Tariff", "fieldname": "total_tariff", "fieldtype": "Float", "width": 120},
		{"label": "ROI", "fieldname": "roi", "fieldtype": "Float", "width": 120},
    ] 
	return columns 

def get_data(filters):
	## Get the avg monthly tariff data
	data=frappe.db.sql("""
		SELECT 
			child.month , child.low_tariff_amount , child.high_tariff_amount , child.total_tariff , parent.purchase_amount
		FROM `tabMonthly Power And Tariff Result` child 
		INNER JOIN `tabSolar Energy Calculation Entry` parent
			ON child.parent = parent.name
		WHERE 
			parent.customer=%s
			AND parent.year=%s
			AND parent.docstatus = 1
	""",(filters.customer , filters.year) , as_dict=1)


	if not data:
		frappe.msgprint("No records found for this customer. Please fill the details")
		return 0

	return data

## Chart configurations
def get_chart_data(data):

	if not data:
		return None
	
	labels= [i.month for i in data]
	low_tariff_data = [i.low_tariff_amount for i in data]
	high_tariff_data = [j.high_tariff_amount for j in data]

	datasets = [
		{
			'name':'Avg Low Tariff',
			'values':low_tariff_data
		},
		{
			'name':'Avg High Tariff',
			'values':high_tariff_data
		}
	]

	## Creating Chart
	return {
		"data":{
			"labels":labels,
			"datasets":datasets
		},
		"type":"bar",
		"colors":["#f9e79f" , "#f8c471"]
	}

