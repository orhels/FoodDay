# coding=UTF-8
from datetime import timedelta, datetime

_weekday_time_slots = (
    (10, 12),
    (13, 15),
    (17, 20),
)

_saturday_time_slots = (
    (10, 16),
)

ONE_DAY = timedelta(days=1)
DAYS = (u'mandag', u'tirsdag', u'onsdag', u'torsdag', u'fredag', u'lørdag', u'søndag')


class Timeslots():
    def __init__(self):
        self._timeslots = []

    def all(self):
        return self._timeslots

    def add(self, day, timeslots):
        self._timeslots.append(Timeslot(day, timeslots))
        return self

    def __eq__(self, other):
        if len(self._timeslots) != len(other._timeslots):
            return False
        for i, e in enumerate(self._timeslots):
            if e != other._timeslots[i]:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)


class Timeslot():
    def __init__(self, day, timeslots):
        self.day = day
        self.timeslots = timeslots

    def __eq__(self, other):
        return self.day == other.day and self.timeslots == other.timeslots

    def __ne__(self, other):
        return not self.__eq__(other)

    def timeslots(self):
        return self.timeslots

    def name(self):
        return DAYS[self.day.weekday()]

    def pretty_date(self):
        return ".".join(map(str, (self.day.day, self.day.month, self.day.year)))



def get_timeslots(weekday):
    if weekday >= 0 and weekday <= 4:
        return _weekday_time_slots
    elif weekday == 5:
        return _saturday_time_slots
    else:
        return []


def get_available_time_slots_for_delivery(today='auto', skip=0, days_ahead=7):
    slots = Timeslots()
    if today == 'auto':
        today = datetime.now().date()
    today = today + (ONE_DAY * skip)
    for days_to_skip in range(days_ahead):
        day = today + (ONE_DAY * days_to_skip)
        timeslots = get_timeslots(day.weekday())
        if timeslots != []:
            slots.add(day, timeslots)
    return slots