// Copyright (c) 2018, Libermatic and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports['Simple Item-Wise Sales Register'] = {
  filters: [
    {
      fieldname: 'from_date',
      label: __('From Date'),
      fieldtype: 'Date',
      default: frappe.datetime.get_today(),
      width: '80',
    },
    {
      fieldname: 'to_date',
      label: __('To Date'),
      fieldtype: 'Date',
      default: frappe.datetime.get_today(),
      width: '80',
    },
    {
      fieldname: 'sales_invoice',
      label: __('Sales Invoice'),
      fieldtype: 'Link',
      options: 'Sales Invoice',
      width: '80',
    },
    {
      fieldname: 'customer',
      label: __('Customer ID'),
      fieldtype: 'Link',
      options: 'Customer',
      width: '80',
    },
  ],
};
