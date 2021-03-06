# Copyright (c) 2013, Indictranstech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	columns = get_colums(filters)
	data = get_data(filters)
	return columns, data

def get_data(filters):
	if filters:

		data= frappe.db.sql("""select so.name,so.customer,so.transaction_date,so.delivery_date,so.grand_total,
					st.sales_person,st.contact_no,st.allocated_percentage,st.allocated_amount,
					st.incentives
					from
  						`tabSales Order` so, `tabSales Team` st
					where
 							st.parent =so.name and st.sales_person='{0}'
					order by so.name desc""".format(filters.sale_person))
		return data
	

	else:
		data= frappe.db.sql("""select so.name,so.customer,so.transaction_date,so.delivery_date,so.grand_total,
					st.sales_person,st.contact_no,st.allocated_percentage,st.allocated_amount,
					st.incentives
					from
  						`tabSales Order` so, `tabSales Team` st
					where
 							st.parent =so.name 
					order by so.name desc""")
		return data 

def get_colums(filters):
	columns =[ ("Sales Order") + ":Link/Sales Order:100",
				   ("Party") + ":230",
				   ("Date") + ":100",
				   ("Delivary Date")+ ":100",
				   ("Sales Amount") + ":Currency:120",
				   ("Sales Person") + ":Data:120",
				   ("Contact No") + ":Data:120",
				   ("Allocated Percentage") + ":Float:120",
				   ("Allocated Amount") + ":Currency:120",
				   ("Incentives") + ":Float:120"


			]
	return columns
