from __future__ import unicode_literals
import frappe
from frappe.model.naming import make_autoname, getseries
from frappe.utils import cstr,get_datetime
from frappe import _
from frappe.utils import money_in_words


@frappe.whitelist()
def validate(self,method=None):
	# for row in self.items:
	# 	if len(self.items) > 8:
	# 		if float(row.idx) % 8 == 0:
	# 			row.page_break = 1

	printformat_net_total = printformat_vat_tax = 0.0
	discount_amount = delivery_charge = 0.0

	for tax in self.taxes:
		if tax.account_head == "Stock Adjustment - E":
			delivery_charge = tax.tax_amount
	if self.discount_amount:
		discount_amount = self.discount_amount

	self.delivery_charge = delivery_charge
	printformat_net_total = (self.total - discount_amount) + delivery_charge
	printformat_vat_tax = (printformat_net_total * 5)/100
	self.printformat_net_total_with_tax = printformat_net_total + printformat_vat_tax
	self.printformat_net_total = printformat_net_total
	self.printformat_vat_tax = printformat_vat_tax
	self.printformat_in_word = money_in_words(self.printformat_net_total_with_tax, self.currency)

	page_break_idx = 7
	for row in self.items:
		if len(self.items) > 6:
			if float(row.idx) == 7:
				row.page_break = 1
				page_break_idx = 7
				page_break_idx = page_break_idx + 11
			elif row.idx >= page_break_idx:
				print "page_break_idx",page_break_idx
				print "row",row.idx
				if float(row.idx) == page_break_idx:
					print "row"
					row.page_break = 1
					page_break_idx = page_break_idx + 11	

@frappe.whitelist()
# def po_submit_notification ():
def po_submit_notification (self,method=None):
	print "\n\n\n\n##########Po trigger"
