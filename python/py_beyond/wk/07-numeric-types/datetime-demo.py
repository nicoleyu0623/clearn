
import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
from util import *
import datetime as dt


def demo_datetime_date():
    banner('datetime dates')
    dt1 = dt.date(year=2014, month=1, day=6) #int as param
    pp(dt1)
    dtn=dt.date.today()
    pp(dtn)
    dt_from_secs = dt.date.fromtimestamp(1000000000)
    pp(dt_from_secs)
    pp('year {} month {} day {}'.format(dtn.year, dtn.month, dtn.day))

    starprint('isoformat')
    pp(dtn.isoformat())
    pp('day {}, weekday {}, isoweekday {}, isoweeeknumber {}'
       .format(dtn.day, dtn.weekday(), dtn.isoweekday(), dtn.isocalendar()[1] ))

    starprint('strftime (formats are platform, interpreter dependent')
    e=dtn.strftime('%A %d %B %Y')
    pp(e)

    starprint('datetime min max')
    pp(dt.date.min)
    pp(dt.date.max)


def demo_datetime_time():
    banner('datetime times')
    pp('time of 3 hours and 1 min: {}'.format(dt.time(3,1))) #all params are ints
    pp('time of 3 hours and 1 min 52 sec 2222 ms: {}'
       .format(dt.time(hour=3,minute=1,second=52,microsecond=2222)))
    tm=dt.time(hour=3,minute=1,second=52,microsecond=22222)
    pp('hour min, sec ms: {} {} {} {}'
       .format(tm.hour, tm.minute, tm.second,tm.microsecond))
    starprint('time isoformat')
    pp(tm.isoformat())
    starprint('time strftime')
    pp(tm.strftime('%H:%M%:%S.%f'))

    pp( "{t.hour}h{t.minute}m{t.second}s.{t.microsecond}ms".format(t=tm))


def demo_datetime_datetime():
    banner('datetime type')
    dtt = dt.datetime(2003,5,12, 14,33,22,23333)
    pp(dtt)

    starprint('datetime.now() returns local machine time')
    dtn = dt.datetime.now()
    pp(dtn)
    starprint('datetime.utcnow()')
    pp(dt.datetime.utcnow())
    starprint('combine date and time ')
    d =dt.date.today()
    t = dt.time(8,15)
    dtc = dt.datetime.combine(d,t)
    pp('combined date time: {}'.format(dtc))

    starprint('create datetime from string with strptime')
    dts = dt.datetime.strptime('2008-09-14 03:05:31.333', '%Y-%m-%d %H:%M:%S.%f')
    pp(dts)

def demo_timedelta():
    banner('time durations and datetime arithmetics')
    a = dt.datetime.now()
    b = dt.datetime.strptime('2019-03-01 03:05:31', '%Y-%m-%d %H:%M:%S')
    pp(a)
    tdelta = a-b
    pp(tdelta) #shows timediff in days, seconds and microseconds
    pp('timedelta total_seconds: {}'.format(tdelta.total_seconds()))

    starprint('add datetime and timedelta')
    a_in_3wks = a + dt.timedelta(weeks=1) * 3
    pp('3 weeks from now: {}'.format(a_in_3wks))

def demo_timezone():
    banner('timezones (highly political subject')
    starprint('flight arrival departure in different timezones')
    cet = dt.timezone(dt.timedelta(hours=1),"CET")
    pp(cet)
    departure = dt.datetime(year=2019, month=7, day=7,
                            hour=11, minute=30, tzinfo=cet)
    arrival = dt.datetime(year=2019, month=7, day=7,
                            hour=12, minute=35, tzinfo=dt.timezone.utc)
    flight_duration = arrival-departure
    pp('departure: {}, arrival: {}, duration of flight:{}'
       .format(departure,arrival,flight_duration))


if __name__ == '__main__':
    demo_datetime_date()
    demo_datetime_time()
    demo_datetime_datetime()
    demo_timedelta()
    demo_timezone()