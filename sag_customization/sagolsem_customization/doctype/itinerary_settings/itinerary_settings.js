// Copyright (c) 2018, Libermatic and contributors
// For license information, please see license.txt

frappe.ui.form.on('Itinerary Settings', {
  refresh: function(frm) {
    frm.fields_dict['expense_account'].get_query = doc => ({
      filters: {
        root_type: 'Expense',
        is_group: false,
      },
    });
    frm.fields_dict['income_account'].get_query = doc => ({
      filters: {
        root_type: 'Income',
        is_group: false,
      },
    });
  },
});
