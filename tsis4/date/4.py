import datetime
def difference(date1,date2):
    datetime.timedelta=date2 - date1
    return datetime.timedelta.days*24*3600 + datetime.timedelta.seconds
date1 = datetime.datetime(year=2022,month=6,day=14)
date2 = datetime.datetime.now()
print(difference(date1,date2), " seconds")
