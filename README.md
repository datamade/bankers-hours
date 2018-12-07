# bankers-hours
Python decorator that will only let a function or method run during specified times


```python
import datetime

import dateutil
from bankershours import within_hours, within_hours_method

TIMEZONE = tz.gettz('America/Chicago')

@within_hours(start_time=datetime.time(9, 0, tzinfo=TIMEZONE),
              end_time=datetime.time(5, 0, tzinfo=TIMEZONE))
def time_sensitive_function():
    ...


class SomeClass(object):

    def __init__(self, start_time, end_time):
        self.start_time = start_time
	self.end_time = end_time

    @within_hours_method
    def time_sensitive_method():
        ...
```
