"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime, timedelta

from django.test import TestCase
from Order.utils import get_available_time_slots_for_delivery, get_timeslots, ONE_DAY, Timeslots, Timeslot


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
thursday_next_week = wednesday_next_week + ONE_DAY


class UtilsTest(TestCase):
    def test_get_available_time_slots_for_delivery_one_day_ahead(self):
        today = tuesday
        result = get_available_time_slots_for_delivery(today=tuesday, days_ahead=1)
        expected = Timeslots().add(today, get_timeslots(today.weekday()))
        self.assertEqual(result, expected)

    def test_get_available_time_slots_for_delivery_with_weekend(self):
        result = get_available_time_slots_for_delivery(today=monday)
        expected = Timeslots()
        days = [monday, tuesday, wednesday, thursday, friday, saturday]
        for day in days:
            expected.add(day, get_timeslots(day.weekday()))
        self.assertEqual(result, expected)

    def test_get_available_time_slots_for_delivery_3_days_from_monday(self):
        result = get_available_time_slots_for_delivery(today=monday, skip=3)
        expected = Timeslots()
        expected_days = [thursday, friday, saturday, monday_next_week, tuesday_next_week, wednesday_next_week]
        for day in expected_days:
            expected.add(day, get_timeslots(day.weekday()))
        self.assertEqual(result, expected)

    def test_pretty_date(self):
        result = Timeslot(datetime(year=2013, month=1, day=7).date(), "").pretty_date()
        expected = "7.1.2013"
        self.assertEqual(result, expected)