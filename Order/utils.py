# coding=UTF-8
from datetime import timedelta, datetime

_weekday_time_slots = (
    (10, 12),
    (13, 15),
    (17, 20),
)

_saturday_time_slots = (
    (10, 16)
)

ONE_DAY = timedelta(days=1)


def get_timeslots(weekday):
    if weekday >= 0 and weekday <= 4:
        return _weekday_time_slots
    elif weekday == 5:
        return _saturday_time_slots
    else:
        return []


def get_available_time_slots_for_delivery(today='auto', skip=0, days_ahead=7):
    slots = []
    if today == 'auto':
        today = datetime.now().date()
    today = today + (ONE_DAY * skip)
    for days_to_skip in range(days_ahead):
        day = today + (ONE_DAY * days_to_skip)
        slots.append({'day': day, 'slots': get_timeslots(day.weekday())})
    return slots