# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def autoname(doc, method):
    if doc.customer_id:
        doc.name = doc.customer_id
        if not doc.mobile_no:
            doc.mobile_no = doc.customer_id
