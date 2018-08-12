// Copyright (c) 2018, Libermatic and contributors
// For license information, please see license.txt

frappe.ui.form.on('Itinerary', {
  onload: async function(frm) {
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
    const { message: accounts = {} } = await frappe.db.get_value(
      'Itinerary Settings',
      null,
      ['expense_account', 'income_account']
    );
    frm.set_value('expense_account', accounts['expense_account']);
    frm.set_value('income_account', accounts['income_account']);
  },
  refresh: function(frm) {
    frappe.ui.form.on('Itinerary Charge', {
      charge_name: async function(frm, cdt, cdn) {
        const { charge_name } = locals[cdt][cdn] || {};
        if (charge_name) {
          const { message: charge } = await frappe.db.get_value(
            'Itinerary Charge Type',
            charge_name,
            'default_value'
          );
          frappe.model.set_value(cdt, cdn, 'amount', charge['default_value']);
        }
      },
      amount: function(frm) {
        frm.trigger('calculate_totals');
      },
      payments_remove: function(frm) {
        frm.trigger('calculate_totals');
      },
    });
  },
  before_save: function(frm) {
    frm.trigger('calculate_totals');
  },
  mode_of_payment: async function(frm) {
    const { mode_of_payment, company } = frm.doc;
    frm.toggle_reqd(['cheque_no', 'cheque_date'], mode_of_payment === 'Cheque');
    frm.toggle_display(
      ['cheque_no', 'cheque_date'],
      mode_of_payment === 'Cheque'
    );
    const { message } = await frappe.call({
      method:
        'erpnext.accounts.doctype.sales_invoice.sales_invoice.get_bank_cash_account',
      args: { mode_of_payment, company },
    });
    if (message) {
      frm.set_value('payment_account', message.account);
    }
  },
  calculate_totals: function(frm) {
    const { payments = [] } = frm.doc;
    const total_charges = payments.reduce((a, { amount: x = 0 }) => a + x, 0);
    const rounded_total = flt(total_charges, 0);
    frm.set_value('total', total_charges);
    frm.set_value('rounding_adjustment', rounded_total - total_charges);
    frm.set_value('rounded_total', rounded_total);
  },
});
