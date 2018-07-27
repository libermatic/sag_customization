# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__

app_name = "sag_customization"
app_title = "Sagolsem Customization"
app_version = __version__
app_publisher = "Libermatic"
app_description = "Customizations for Sagolsem Enterprises"
app_icon = "fa fa-mobile-alt"
app_color = "#F44336"
app_email = "info@libermatic.com"
app_license = "MIT"

fixtures = [
    {
        'doctype': 'Property Setter',
        'filters': [['name', 'in', [
            'Customer-customer_name-in_standard_filter',
            'Customer-territory-in_list_view',
            'Sales Invoice-is_pos-default',
            'Sales Invoice-time_sheet_list-hidden',
            'Sales Invoice-timesheets-hidden',
            'Sales Invoice-total_net_weight-hidden',
            'Sales Invoice-taxes_section-hidden',
            'Sales Invoice-taxes_and_charges-hidden',
            'Sales Invoice-shipping_rule-hidden',
            'Sales Invoice-taxes-hidden',
            'Sales Invoice-sec_tax_breakup-hidden',
            'Sales Invoice-other_charges_calculation-hidden',
            'Sales Invoice-base_total_taxes_and_charges-hidden',
            'Sales Invoice-total_taxes_and_charges-hidden',
            'Sales Invoice-gst_section-collapsible',
        ]]],
    },
    {
        'doctype': 'Custom Field',
        'filters': [['name', 'in', [
            'Customer-customer_id',
            'Sales Invoice Payment-reference_no',
            'Sales Invoice Payment-reference_date',
        ]]],
    },
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sag_customization/css/sag_customization.css"
# app_include_js = "/assets/sag_customization/js/sag_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/sag_customization/css/sag_customization.css"
# web_include_js = "/assets/sag_customization/js/sag_customization.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#   "Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sag_customization.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sag_customization.install.before_install"
# after_install = "sag_customization.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = \
#   "sag_customization.notifications.get_notification_config"

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
    'Customer': {
        'autoname': 'sag_customization.doc_events.customer.autoname',
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sag_customization.tasks.all"
# 	],
# 	"daily": [
# 		"sag_customization.tasks.daily"
# 	],
# 	"hourly": [
# 		"sag_customization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sag_customization.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sag_customization.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sag_customization.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
#   "frappe.desk.doctype.event.event.get_events": \
#      "sag_customization.event.get_events"
# }
