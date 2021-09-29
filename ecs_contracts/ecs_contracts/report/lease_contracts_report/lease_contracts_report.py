# Copyright (c) 2013, erpcloud.systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	data=get_data(filters,columns)
	return columns, data

def get_columns():
	return [
		{
			"label": _("Contract No"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Lease Contract",
			"width": 155
		},
		{
			"label": _("Party"),
			"fieldname": "party_name",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("Posting Date"),
			"fieldname": "posting_date",
			"fieldtype": "Date",
			"width": 105
		},
		{
			"label": _("Contract Period In Months"),
			"fieldname": "no_of_months",
			"fieldtype": "Data",
			"width": 220
		},
		{
			"label": _("Start Date"),
			"fieldname": "start_date",
			"fieldtype": "Date",
			"width": 100
		},
		{
			"label": _("End Date"),
			"fieldname": "end_date",
			"fieldtype": "Date",
			"width": 100
		},
		{
			"label": _("Unit Type"),
			"fieldname": "unit_type",
			"fieldtype": "Data",
			"width": 110
		},
		{
			"label": _("Rent Amount"),
			"fieldname": "rent_value_",
			"fieldtype": "Currency",
			"width": 140
		},
		{
			"label": _("Annual Increase %"),
			"fieldname": "annual_increase",
			"fieldtype": "Percent",
			"width": 160
		},
		{
			"label": _("Annual Increase Type"),
			"fieldname": "annual_increase_type",
			"fieldtype": "Data",
			"width": 160
		},
		{
			"label": _("Insurance Amount"),
			"fieldname": "insurance_value",
			"fieldtype": "Currency",
			"width": 160
		},
		{
			"label": _("Total Payable Amount"),
			"fieldname": "total_payable_amount",
			"fieldtype": "Currency",
			"width": 160
		},
		{
			"label": _("Total Amount Paid"),
			"fieldname": "total_amount_paid",
			"fieldtype": "Currency",
			"width": 160
		}
	]

def get_data(filters, columns):
	item_price_qty_data = []
	item_price_qty_data = get_item_price_qty_data(filters)
	return item_price_qty_data

def get_item_price_qty_data(filters):
	conditions = ""
	if filters.get("contract"):
		conditions += " and a.name=%(contract)s"
	if filters.get("unit_type"):
		conditions += " and a.unit_type=%(unit_type)s"
	if filters.get("from_date"):
		conditions += " and a.posting_date>=%(from_date)s"
	if filters.get("to_date"):
		conditions += " and a.posting_date<=%(to_date)s"
	item_results = frappe.db.sql("""
				select
						a.name as name,
						a.party_name as party_name,
						a.posting_date as posting_date,
						a.unit_type as unit_type,
						a.no_of_months as no_of_months,
						a.rent_value_ as rent_value_,
						a.annual_increase as annual_increase,
						a.annual_increase_type as annual_increase_type,
						a.start_date as start_date,
						a.end_date as end_date,
						a.total_payable_amount as total_payable_amount,
						a.total_amount_paid as total_amount_paid,	
						a.insurance_value as insurance_value				
				from `tabLease Contract` a 
				where
					 a.docstatus = 1
					{conditions}
				""".format(conditions=conditions), filters, as_dict=1)


	#price_list_names = list(set([item.price_list_name for item in item_results]))

	#buying_price_map = get_price_map(price_list_names, buying=1)
	#selling_price_map = get_price_map(price_list_names, selling=1)

	result = []
	if item_results:
		for item_dict in item_results:
			data = {
				'name': item_dict.name,
				'party_name': item_dict.party_name,
				'unit_type': item_dict.unit_type,
				'posting_date': item_dict.posting_date,
				'no_of_months': item_dict.no_of_months,
				'rent_value_': item_dict.rent_value_,
				'annual_increase': item_dict.annual_increase,
				'annual_increase_type': item_dict.annual_increase_type,
				'start_date': item_dict.start_date,
				'end_date': item_dict.end_date,
				'total_payable_amount': item_dict.total_payable_amount,
				'total_amount_paid': item_dict.total_amount_paid,
				'insurance_value': item_dict.insurance_value,
			}
			result.append(data)

	return result

def get_price_map(price_list_names, buying=0, selling=0):
	price_map = {}

	if not price_list_names:
		return price_map

	rate_key = "Buying Rate" if buying else "Selling Rate"
	price_list_key = "Buying Price List" if buying else "Selling Price List"

	filters = {"name": ("in", price_list_names)}
	if buying:
		filters["buying"] = 1
	else:
		filters["selling"] = 1

	pricing_details = frappe.get_all("Item Price",
		fields = ["name", "price_list", "price_list_rate"], filters=filters)

	for d in pricing_details:
		name = d["name"]
		price_map[name] = {
			price_list_key :d["price_list"],
			rate_key :d["price_list_rate"]
		}

	return price_map
