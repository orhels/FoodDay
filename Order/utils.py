# coding=UTF-8
from datetime import timedelta, datetime

_weekday_time_slots = (
    (9, 11),
    (12, 15),
    (17, 21),
)

_saturday_time_slots = (
    (10, 16),
)

ONE_DAY = timedelta(days=1)
DAYS = (u'mandag', u'tirsdag', u'onsdag', u'torsdag', u'fredag', u'lørdag', u'søndag')


def get_timeslots(weekday):
    if weekday >= 0 and weekday <= 4:
        return _weekday_time_slots
    elif weekday == 5:
        return _saturday_time_slots
    else:
        return ()


def get_available_time_slots_for_delivery(today='auto', skip=1, days_ahead=7):
    slots = []
    if today == 'auto':
        today = datetime.now()
    today = today + (ONE_DAY * skip)
    for days_to_skip in range(days_ahead):
        day = today + (ONE_DAY * days_to_skip)
        timeslots = get_timeslots(day.weekday())
        if len(timeslots) != 0:
            slots.append({'date': format_date(day), 'timeslots': timeslots})
    return slots


def format_date(datetime):
    return datetime.strftime("%d.%m.%Y")