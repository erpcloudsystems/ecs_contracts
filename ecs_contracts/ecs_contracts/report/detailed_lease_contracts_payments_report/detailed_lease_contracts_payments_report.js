// Copyright (c) 2016, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Detailed Lease Contracts Payments Report"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80"
		},
		{
			"fieldname":"contract",
			"label": __("Contract No"),
			"fieldtype": "Link",
			"options":  "Lease Contract",
		},
		{
			"fieldname":"is_paid",
			"label": __("Is Paid"),
			"fieldtype": "Check",
		},
	],
};