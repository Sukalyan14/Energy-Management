// Copyright (c) 2025, Sukalyan and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Year Tariff Cost"] = {
	"filters": [
		{
			fieldname: 'customer',
			label: __('Customer Name'),
			fieldtype: 'Link',
			options: 'Customer',
		},
		{
			fieldname: 'year',
			label:__('Year'),
			fieldtype: 'Int',
			default: new Date().getFullYear() 
		}
	]
};
