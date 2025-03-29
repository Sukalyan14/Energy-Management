# Copyright (c) 2025, Sukalyan and contributors
# For license information, please see license.txt

import frappe
import datetime
from frappe.model.document import Document
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from frappe.utils import getdate

class PowerConsumptionEntry(Document):
	def validate(doc):
		# Check purchase date and entry date 
		dateCheck(doc.purchase_date , doc.entry_date)
		
		# Preventing a new record to be created/updated for same customer , for same date and same tariff type
		checkDuplicateRecord(doc.name , doc.customer , doc.entry_date , doc.is_low_tariff)

# Checking Purchase Date
def dateCheck(purchase_date , entry_date):
	## To check if dates are in correct format . 
	if isinstance(purchase_date , str):
		purchase_date = getdate(purchase_date)

	if isinstance(entry_date , str):
		entry_date = getdate(entry_date)
		
	# prevent saving if data entry date if before purchase data
	if entry_date < purchase_date:
		frappe.throw("Entry Date Cannot be before purchase date-%s" %purchase_date)


def checkDuplicateRecord(name , customer , entry_date , is_low_tariff):
	existing_records = frappe.get_all('Power Consumption Entry' , { 
												'customer':customer ,
												'entry_date':entry_date ,
												'is_low_tariff':is_low_tariff ,
												'name':('!=' , name)} ,
											)
	if existing_records:
		frappe.throw("A record with same Customer name , Entry Date and Tariff Check Already Exists")
	