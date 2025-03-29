// Copyright (c) 2025, Sukalyan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Power Consumption Entry', {
	refresh:function(frm){
		if(frm.doc.purchase_date){
			frm.fields_dict.entry_date.datepicker.update({
				minDate: new Date(frm.doc.purchase_date),
			});
		}
		
	},
	// Check for preventing of selecting a date ahead of purchase date and also clear date entry if it already has a date
	customer: function(frm){
		if(frm.doc.entry_date){
			frm.set_value('entry_date',"")	
		} 
		//prevents the user from selecting a date past of the purchase date 
		frm.fields_dict.entry_date.datepicker.update({
			minDate: new Date(frm.doc.purchase_date),
		});
	},

});
