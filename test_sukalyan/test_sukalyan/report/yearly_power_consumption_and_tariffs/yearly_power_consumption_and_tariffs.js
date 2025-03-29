// Copyright (c) 2025, Sukalyan and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Yearly Power Consumption And Tariffs"] = {
	"filters": [
		{
			fieldname: 'customer',
			label: __('Customer Name'),
			fieldtype: 'Link',
			options: 'Customer',
		},
		{
			fieldname: 'year',
			label:_('Year'),
			fieldtype: 'Int',
			// length:4
		}
	]
};
