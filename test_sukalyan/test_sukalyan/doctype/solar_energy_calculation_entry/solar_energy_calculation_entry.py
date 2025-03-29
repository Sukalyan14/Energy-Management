# Copyright (c) 2025, Sukalyan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SolarEnergyCalculationEntry(Document):
	def validate(doc):
		
		## Only when creating a new record
		if doc.is_new():

			## Check for any existing  data calucation entry entry
			last_series = frappe.db.sql("""
				SELECT MAX(calculation_series) 
				FROM `tabSolar Energy Calculation Entry`
				WHERE customer=%s
		""", doc.customer)
			
			## If not data was found or record being created for the first time. To prevent None 
			if not last_series:
				# print("n\n\n\nhere" , last_series[0][0] , doc.calculation_series)
				doc.calculation_series = last_series[0][0] + 1	
			
		calculate_monthly_results(doc)

def calculate_monthly_results(doc):
	
	## Clear the table for any existing/non used data
	doc.monthly_results = []
	
	## Getting the list of months from select field options
	month_name = frappe.get_meta("Monthly Power And Tariff Result").get_field("month").options.strip().split('\n') 
	
	for month in range(1,13):

		## Fetching entry date and readings
		data = frappe.db.sql("""
				SELECT entry_date , kw_reading , kwh_reading , is_low_tariff
				FROM `tabPower Consumption Entry` 
				WHERE
					customer=%s  
					AND DATE_FORMAT(entry_date , '%%Y')=%s
					AND DATE_FORMAT(entry_date , '%%c')=%s
			""" , (doc.customer , doc.year , month), as_dict = 1)
		
		## Clear the empty results
		if not data:
			continue
		
		## Calucate avg power consumptions
		avg_kw = sum(d['kw_reading'] for d in data) / len(data)
		avg_kwh = sum(d['kwh_reading'] for d in data) / len(data)

		## Calculate tariff amounts
		low_tariff_readings = []
		high_tarif_readings = []

		## sorting data based on high and low tariff
		for i in data:
			if i['is_low_tariff'] == 1:
				low_tariff_readings.append(i['kwh_reading'])
			else:
				high_tarif_readings.append(i['kwh_reading'])

		if low_tariff_readings:
			low_tariff_cost = 0.1 * sum(low_tariff_readings) / len(low_tariff_readings)
		else:
			low_tariff_cost = 0

		if high_tarif_readings:
			high_tarif_cost = 0.3 * sum(high_tarif_readings) / len(high_tarif_readings)
		else:
			high_tarif_cost = 0
		# print("\n\n\n", data ,month_name[0] , month)
		## Creating an entry in the child table		
		doc.append("monthly_results" , {
			"month":month_name[month - 1],
			"avg_kw":avg_kw,
			"avg_kwh":avg_kwh,
			"low_tariff_amount":low_tariff_cost,
			"high_tariff_amount":high_tarif_cost,
			"total_tariff":low_tariff_cost + high_tarif_cost
		})



