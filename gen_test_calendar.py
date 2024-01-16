""" utcrcalendar : generate UTCr responsible calendars
"""
import datetime
import icalendar
from icalendar.tools import UIDGenerator


start = datetime.datetime(2024, 1, 1, 10, tzinfo=datetime.timezone.utc)
stop = datetime.datetime(2024, 12, 31, tzinfo=datetime.timezone.utc)
step = datetime.timedelta(days=1)


cal = icalendar.Calendar()
cal.add('prodid', '-//Test calendar//fm//')
cal.add('version', '2.0')
cal.add('summary', 'UTCr calendar')

dt = start
while dt < stop:
    event = icalendar.Event()
    event.add('summary', 'A short summary')
    event.add('uid', UIDGenerator.uid("@bar.org"))
    event.add('dtstart', dt)
    event.add('dtend', dt + datetime.timedelta(hours=2))
    event.add('organizer', 'MAILTO:foo@bar.org')
    cal.add_component(event)
    dt += step

with open("test_calendar.ics", 'wb') as fp:
    fp.write(cal.to_ical())
