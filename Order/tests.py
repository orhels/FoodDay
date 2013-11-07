"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime, timedelta

from django.test import TestCase
from Order.utils import get_available_time_slots_for_delivery, format_date, _weekday_time_slots, _saturday_time_slots


class UtilsTest(TestCase):
    def test_get_available_time_slots_for_delivery_seven_days_ahead(self):
        result = get_available_time_slots_for_delivery(today=datetime(2013, 1, 7))
        expect = [
            {'date': format_date(datetime(2013, 1, 8)),
             'timeslots': (_weekday_time_slots)
            },
            {'date': format_date(datetime(2013, 1, 9)),
             'timeslots': (_weekday_time_slots)
            },
            {'date': format_date(datetime(2013, 1, 10)),
             'timeslots': (_weekday_time_slots)
            },
            {'date': format_date(datetime(2013, 1, 11)),
             'timeslots': (_weekday_time_slots)
            },
            {'date': format_date(datetime(2013, 1, 12)),
             'timeslots': (_saturday_time_slots)
            },
            {'date': format_date(datetime(2013, 1, 14)),
             'timeslots': (_weekday_time_slots)
            },
        ]
        self.assertEqual(result, expect)