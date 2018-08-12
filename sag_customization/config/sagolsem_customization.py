# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Transactions"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Itinerary",
                    "label": "Itinerary",
                    "description": _("Itinerary"),
                },
            ]
        },
        {
            "label": _("Setup"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Itinerary Charge Type",
                    "label": "Itinerary Charge Type",
                    "description": _("Itinerary Charge Type"),
                },
                {
                    "type": "doctype",
                    "name": "Itinerary Settings",
                    "label": "Itinerary Settings",
                    "description": _("Global itinerary configuration"),
                },
            ]
        },
    ]
