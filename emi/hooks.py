# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "emi"
app_title = "Emi"
app_publisher = "Indictranstech"
app_description = "Manufacturing Ladder"
app_icon = "octicon octicon-file-directory"
app_color = "Blue"
app_email = "sagar.s@indictranstech.com"
app_license = "INDICTRANS"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/emi/css/c3.css"
# app_include_js = "/assets/emi/js/c3.min.js"
# app_include_js = "/assets/js/telecom_v7.js"
# include js, css files in header of web template
# web_include_css = "/assets/emi/css/emi.css"
# web_include_js = "/assets/emi/js/emi.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "emi.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "emi.install.before_install"
#after_install = ["emi.emi.custom_methods.after_install_process_add","emi.emi.custom_methods.after_install_warehouse_add"]

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "emi.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events


doc_events = {
	"Sales Invoice": {
		"validate": ["emi.emi.custom_methods.validate_delivery_note",
            "emi.emi.custom_methods.validate_si","emi.custom_script.sales_invoice.sales_invoice.validate"],
        "on_submit":"emi.custom_script.sales_invoice.sales_invoice.SI_submit_notification"
	},

	('Quotation', 'Sales Order'): {
		"validate": ["emi.emi.custom_methods.calulate_consolidated_margin",
            "emi.custom_script.quotation.quotation.validate"],
	},
	"Stock Ledger Entry" :{
		"before_submit": "emi.emi.custom_methods.get_requested_for"
	},
	"Delivery Note": {
        "on_submit": "emi.custom_script.delivery_note.delivery_note.on_submit",
        "validate": "emi.custom_script.delivery_note.delivery_note.validate"
    },
    "Stock Entry":{
        "on_submit": "emi.custom_script.stock_entry.stock_entry.on_submit",
        "validate": "emi.custom_script.stock_entry.stock_entry.validate",
    },
	"Purchase Receipt":{
        "on_submit": "emi.custom_script.purchase_receipt.purchase_receipt.on_submit",
        "validate": "emi.custom_script.purchase_receipt.purchase_receipt.validate"
    },
    "Sales Order":{
        "on_submit":["emi.emi.custom_methods.send_email_sales_person",
                    "emi.emi.custom_methods.sales_order_submit_notification"],
        "validate":"emi.custom_script.sales_order.sales_order.validate",
    },
    "Quotation":{
        "on_submit":"emi.emi.custom_methods.quotation_submit_notification",
    },
    "Purchase Order": {
        "validate": "emi.custom_script.purchase_order.purchase_order.validate",
        "on_submit": "emi.custom_script.purchase_order.purchase_order.po_submit_notification"
    },
    "Purchase Invoice": {
        "on_submit": "emi.custom_script.purchase_invoice.purchase_invoice.PI_submit_notification"
    },
    "Production Order": {
       "on_submit": "emi.custom_script.production_order.production_order.notify_to_qty_manager",
    },
    "Quality Inspection": {
        "on_submit": "emi.custom_script.quality_inspection.quality_inspection.notify_to_qc_manager",
    }
    
}

doctype_js = {
    "Quotation":["custom_script/quotation/quotation.js"],
    "Sales Order" :["custom_script/sales_order/sales_order.js"],
    "Sales Invoice":["custom_script/sales_invoice/sales_invoice.js"],
    "Purchase Receipt":["custom_script/purchase_receipt/purchase_receipt.js"],
    "Purchase Invoice":["custom_script/purchase_invoice/purchase_invoice.js"],
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"emi.tasks.all"
# 	],
# 	"daily": [
# 		"emi.tasks.daily"
# 	],
# 	"hourly": [
# 		"emi.tasks.hourly"
# 	],
# 	"weekly": [
# 		"emi.tasks.weekly"
# 	]
# 	"monthly": [
# 		"emi.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "emi.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
override_whitelisted_methods = {
	"erpnext.manufacturing.doctype.production_order.production_order.make_stock_entry": "emi.emi.custom_methods.make_stock_entry"
}
fixtures = ["Web Form","Custom Field","Print Format","Property Setter","Letter Head","Report","Custom Script","Address Template"]
