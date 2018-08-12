# -*- coding: utf-8 -*-
# Copyright (c) 2018, Libermatic and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import money_in_words
from erpnext.controllers.accounts_controller import AccountsController
from erpnext.accounts.general_ledger import make_gl_entries


class Itinerary(AccountsController):
    def before_save(self):
        if self.mode_of_payment != 'Cheque':
            self.cheque_no = None
            self.cheque_date = None
        currency = frappe.db.get_value(
            'Company', self.company, 'default_currency'
        )
        self.in_words = money_in_words(self.rounded_total, currency)

    def on_submit(self):
        self.make_gl_entries()

    def on_cancel(self):
        self.make_gl_entries(cancel=1)

    def make_gl_entries(self, cancel=0, adv_adj=0):
        cost_center, round_off_account = frappe.db.get_value(
            'Company',
            self.company,
            ['cost_center', 'round_off_account'],
        )
        gl_entries = [
            self.get_gl_dict({
                'account': self.income_account,
                'credit': self.total,
                'cost_center': cost_center,
            }),
            self.get_gl_dict({
                'account': self.payment_account,
                'debit': self.rounded_total,
            }),
        ]
        if self.rounding_adjustment:
            gl_entries.append(
                self.get_gl_dict({
                    'account': round_off_account,
                    'credit': self.rounding_adjustment,
                    'cost_center': cost_center,
                }),
            )
        make_gl_entries(
            gl_entries, cancel=cancel, adv_adj=adv_adj, merge_entries=False
        )
