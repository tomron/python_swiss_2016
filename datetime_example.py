from datetime import datetime

# from string
my_time = '2016-02-05 09:37:11'
print datetime.strptime(my_time, "%Y-%m-%d %H:%M:%S")

# to string
now = datetime.now()
print now.strftime("%Y-%B-%d %H:%M:%S")

from datetime import timedelta

delta = timedelta(hours=1)
time_in_1_hour = now + delta
print now
print time_in_1_hour

and_now = datetime.now()

# who much time passed?
time_diff = and_now - now
print "time_diff: %s"%time_diff
print "time_diff.seconds: %s"%time_diff.seconds
print "time_diff.total_seconds: %s"%time_diff.total_seconds()

tomorrow = now + timedelta(days=1)
time_diff_tomorrow = tomorrow - now
print "time_diff_tomorrow: %s"%time_diff_tomorrow
print "time_diff_tomorrow.seconds: %s"%time_diff_tomorrow.seconds
print "time_diff_tomorrow.total_seconds: %s"%time_diff_tomorrow.total_seconds()
