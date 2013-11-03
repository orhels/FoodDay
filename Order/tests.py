"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime, timedelta

from django.test import TestCase
from Order.utils import get_available_time_slots_for_delivery, get_timeslots, ONE_DAY


class UtilsTest(TestCase):
    def test_get_available_time_slots_for_delivery_one_day_ahead(self):
        today = datetime.now().date()
        result = get_available_time_slots_for_delivery(days_ahead=1)
        expected = [{'day': today, 'slots': get_timeslots(today.weekday())}]
        self.assertEqual(result, expected)

    def test_get_available_time_slots_for_delivery_three_days_ahead(self):
        today = datetime.now().date()
        tomorrow = datetime.now().date() + timedelta(days=1)
        the_day_after_tomorrow = datetime.now().date() + timedelta(days=2)
        result = get_available_time_slots_for_delivery(days_ahead=3)
        expected = [
            {'day': today, 'slots': get_timeslots(today.weekday())},
            {'day': tomorrow, 'slots': get_timeslots(tomorrow.weekday())},
            {'day': the_day_after_tomorrow, 'slots': get_timeslots(the_day_after_tomorrow.weekday())},
        ]
        self.assertEqual(result, expected)

    def test_get_available_time_slots_for_delivery_with_weekend(self):
        monday = datetime(year=2013, month=1, day=7).date()
        tuesday = monday + ONE_DAY
        wednesday = tuesday + ONE_DAY
        thursday = wednesday + ONE_DAY
        friday = thursday + ONE_DAY
        saturday = friday + ONE_DAY
        sunday = saturday + ONE_DAY

        result = get_available_time_slots_for_delivery(today=monday)
        expected = [
            {'day': monday, 'slots': get_timeslots(monday.weekday())},
            {'day': tuesday, 'slots': get_timeslots(tuesday.weekday())},
            {'day': wednesday, 'slots': get_timeslots(wednesday.weekday())},
            {'day': thursday, 'slots': get_timeslots(thursday.weekday())},
            {'day': friday, 'slots': get_timeslots(friday.weekday())},
            {'day': saturday, 'slots': get_timeslots(saturday.weekday())},
            {'day': sunday, 'slots': get_timeslots(sunday.weekday())},
        ]
        self.assertEqual(result, expected)

    def test_get_available_time_slots_for_delivery_3_days_from_monday(self):
        monday = datetime(year=2013, month=1, day=7).date()
        tuesday = monday + ONE_DAY
        wednesday = tuesday + ONE_DAY
        thursday = wednesday + ONE_DAY
        friday = thursday + ONE_DAY
        saturday = friday + ONE_DAY
        sunday = saturday + ONE_DAY
        monday_next_week = sunday + ONE_DAY
        tuesday_next_week = monday_next_week + ONE_DAY
        wednesday_next_week = tuesday_next_week + ONE_DAY

        result = get_available_time_slots_for_delivery(today=monday, skip=3)
        expected = [
            {'day': thursday, 'slots': get_timeslots(thursday.weekday())},
            {'day': friday, 'slots': get_timeslots(friday.weekday())},
            {'day': saturday, 'slots': get_timeslots(saturday.weekday())},
            {'day': sunday, 'slots': get_timeslots(sunday.weekday())},
            {'day': monday_next_week, 'slots': get_timeslots(monday_next_week.weekday())},
            {'day': tuesday_next_week, 'slots': get_timeslots(tuesday_next_week.weekday())},
            {'day': wednesday_next_week, 'slots': get_timeslots(wednesday_next_week.weekday())}
        ]
        self.assertEqual(result, expected)