# Copyright (c) 2018, Libermatic and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters={}):
    columns = [
        _('Posting Date') + ':Date:80',
        _('Item Code') + ':Link/Item:100',
        _('Item Group') + ':Link/Item Group:100',
        _('More Description') + '::150',
        _('Amount') + ':Currency/currency:120',
        _('Invoice') + ':Link/Sales Invoice:120',
        _('Customer') + ':Link/Customer:120',
        _('Customer Name') + '::120'
    ]
    conds = [
        'invoice.docstatus = 1',
        "invoice.posting_date BETWEEN '{}' AND '{}'".format(
            filters.get('from_date'), filters.get('to_date')
        )
    ]
    conds_map = {
        'sales_invoice': "invoice.name = '{}'",
        'customer': "invoice.customer = '{}'",
    }
    for key, query in conds_map.items():
        if filters.get(key):
            conds.append(query.format(filters.get(key)))
    data = frappe.db.sql("""
        SELECT
            invoice.posting_date,
            item.item_code,
            item.item_group,
            item.more_description,
            item.amount,
            invoice.name,
            invoice.customer,
            invoice.customer_name
        FROM `tabSales Invoice` AS invoice, `tabSales Invoice Item` AS item
        WHERE invoice.name = item.parent AND %s
        ORDER BY invoice.posting_date ASC, invoice.name ASC
        """ % ' AND '.join(conds))
    return columns, data
