import datetime

h, m = map(int, input().split())

alarm_time = datetime.datetime(2020, 1, 1, h, m)
min_45 = datetime.timedelta(minutes=45)

result = alarm_time - min_45
print('{} {}'.format(result.hour, result.minute))
