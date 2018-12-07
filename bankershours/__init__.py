import datetime
import logging

from dateutil import tz

logger = logging.getLogger(__name__)

def within_hours_method(func):
    def wrapper(self, *args, **kwargs):
        now = datetime.datetime.now(tz.tzutc())
        start_dt = datetime.datetime.combine(datetime.date.today(), 
                                             self.start_time)
        end_dt = datetime.datetime.combine(datetime.date.today(), 
                                             self.end_time)
        if start_dt < end_dt:
            if start_dt < now < end_dt:
                return func(self, *args, **kwargs)
            elif now < start_dt:
                scheduled_dt = start_dt
            elif now > end_dt:
                scheduled_dt = start_dt + datetime.timedelta(days=1)

        if end_dt < start_dt:
            if now < end_dt:
                return func(self, *args, **kwargs)
            else:
                scheduled_dt = start_dt
                          
        sleep_for = scheduled_time - now
        logger.info('Sleeping for a while, {}'.format(sleep_for))
        time.sleep(sleep_for.total_seconds())
        return func(self, *args, **kwargs)

    return wrapper


def within_hours(func, start_time=None, end_time=None):
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now(tz.tzutc())
        start_dt = datetime.datetime.combine(datetime.date.today(), 
                                             start_time)
        end_dt = datetime.datetime.combine(datetime.date.today(), 
                                           end_time)
        if start_dt < end_dt:
            if start_dt < now < end_dt:
                return func(*args, **kwargs)
            elif now < start_dt:
                scheduled_dt = start_dt
            elif now > end_dt:
                scheduled_dt = start_dt + datetime.timedelta(days=1)

        if end_dt < start_dt:
            if now < end_dt:
                return func(*args, **kwargs)
            else:
                scheduled_dt = start_dt
                          
        sleep_for = scheduled_time - now
        logger.info('Sleeping for a while, {}'.format(sleep_for))
        time.sleep(sleep_for.total_seconds())
        return func(*args, **kwargs)

    return wrapper
