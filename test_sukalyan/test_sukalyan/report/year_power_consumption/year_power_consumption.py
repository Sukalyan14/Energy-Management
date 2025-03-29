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
        {"label": "Avg. KW", "fieldname": "avg_kw", "fieldtype": "Float", "width": 120},
		{"label": "Avg KWH", "fieldname": "avg_kwh", "fieldtype": "Float", "width": 120},
    ] 
	return columns 

def get_data(filters):
	
	data=frappe.db.sql("""
		SELECT 
			child.month , child.avg_kw , child.avg_kwh 
		FROM `tabMonthly Power And Tariff Result` child 
		INNER JOIN `tabSolar Energy Calculation Entry` parent
			ON child.parent = parent.name
		WHERE 
			parent.customer=%s
			AND parent.year=%s
			AND parent.docstatus = 1
	""",(filters.customer , filters.year) , as_dict=1)
	
	return data

def get_chart_data(data):

	if not data:
		return None
	
	labels= [i.month for i in data]
	kw_values = [i.avg_kw for i in data]
	kwh_values = [j.avg_kwh for j in data]

	datasets = [
		{
			'name':'Avg Kw Consumption',
			'values':kw_values
		},
		{
			'name':'Avg KwH Consumption',
			'values':kwh_values
		}
	]

	## Creating Chart
	return {
		"data":{
			"labels":labels,
			"datasets":datasets
		},
		"type":"bar",
		"colors":["#76d7c4" , "#117a65 "]
	}