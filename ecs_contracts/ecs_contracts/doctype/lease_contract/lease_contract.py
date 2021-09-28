# Copyright (c) 2021, ERP Cloud Systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, json
from frappe.model.document import Document
from frappe import _
from frappe.desk.search import sanitize_searchfield
from frappe.utils import (flt, getdate, get_url, now,
nowtime, get_time, today, get_datetime, add_days)
from frappe.utils import add_to_date, now, nowdate
import frappe, math, json
import erpnext
from frappe import _
from six import string_types
from frappe.utils import flt, rounded, add_months, nowdate, getdate, now_datetime

class LeaseContract(Document):
	@frappe.whitelist()
	def validate(self):
		self.calculate_repayment_schedule()

	@frappe.whitelist()
	def calculate_repayment_schedule(self):
		self.contract_repayment_schedule = []
		payment_date = self.start_date
		self.end_date = add_months(payment_date, self.no_of_months)
		monthly_payment = self.rent_value_
		fixed_value = self.rent_value_ * self.annual_increase / 100
		a = self.no_of_months
		b = 1
		x = self.rent_value_ + fixed_value
		x1 = x + (x * self.annual_increase / 100)
		x2 = x1 + (x1 * self.annual_increase / 100)
		x3 = x2 + (x2 * self.annual_increase / 100)
		x4 = x3 + (x3 * self.annual_increase / 100)
		x5 = x4 + (x4 * self.annual_increase / 100)
		x6 = x5 + (x5 * self.annual_increase / 100)
		x7 = x6 + (x6 * self.annual_increase / 100)
		x8 = x7 + (x7 * self.annual_increase / 100)
		x9 = x8 + (x8 * self.annual_increase / 100)
		x10 = x9 + (x9 * self.annual_increase / 100)
		x11 = x10 + (x10 * self.annual_increase / 100)
		x12 = x11 + (x11 * self.annual_increase / 100)
		x13 = x12 + (x12 * self.annual_increase / 100)
		x14 = x13 + (x13 * self.annual_increase / 100)
		x15 = x14 + (x14 * self.annual_increase / 100)
		x16 = x15 + (x15 * self.annual_increase / 100)
		x17 = x16 + (x16 * self.annual_increase / 100)
		x18 = x17 + (x17 * self.annual_increase / 100)
		x19 = x18 + (x18 * self.annual_increase / 100)


		while (a > 0):
			self.append("contract_repayment_schedule", {
				"payment_date": payment_date,
				"monthly_payment": monthly_payment
			})
			next_payment_date = add_months(payment_date, 1)
			payment_date = next_payment_date

			if b >= 12 and b <= 23:
				rent_value = x
				monthly_payment = rent_value

			if b >= 24 and b <= 35:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (2 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x1
					monthly_payment = rent_value

			if b >= 36 and b <= 47:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (3 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x2
					monthly_payment = rent_value

			if b >= 48 and b <= 59:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (4 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x3
					monthly_payment = rent_value

			if b >= 60 and b <= 71:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (5 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x4
					monthly_payment = rent_value

			if b >= 72 and b <= 83:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (6 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x5
					monthly_payment = rent_value

			if b >= 84 and b <= 95:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (7 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x6
					monthly_payment = rent_value

			if b >= 96 and b <= 107:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (8 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x7
					monthly_payment = rent_value

			if b >= 108 and b <= 119:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (9 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x8
					monthly_payment = rent_value

			if b >= 120 and b <= 131:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (10 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x9
					monthly_payment = rent_value

			if b >= 132 and b <= 143:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (11 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x10
					monthly_payment = rent_value

			if b >= 144 and b <= 155:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (12 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x11
					monthly_payment = rent_value

			if b >= 156 and b <= 167:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (13 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x12
					monthly_payment = rent_value

			if b >= 168 and b <= 179:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (14 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x13
					monthly_payment = rent_value

			if b >= 180 and b <= 191:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (15 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x14
					monthly_payment = rent_value

			if b >= 192 and b <= 203:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (16 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x15
					monthly_payment = rent_value

			if b >= 204 and b <= 215:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (17 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x16
					monthly_payment = rent_value

			if b >= 216 and b <= 227:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (18 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x17
					monthly_payment = rent_value

			if b >= 228 and b <= 239:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (19 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x18
					monthly_payment = rent_value

			if b >= 240 and b <= 251:
				if self.annual_increase_type == "Fixed Rate":
					rent_value = self.rent_value_ + (20 * fixed_value)
					monthly_payment = rent_value

				if self.annual_increase_type == "Accumulated Rate":
					rent_value = x19
					monthly_payment = rent_value

			b += 1
			a -= 1

	pass
