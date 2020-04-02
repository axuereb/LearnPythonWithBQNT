import datetime

dt = '12-Nov-17 13:30'

new_dt = datetime.datetime.strptime(dt, "%d-%b-%y %H:%M") - datetime.timedelta(seconds=250)

new_dt.strftime("%Y-%m-%d %H:%M:%S")