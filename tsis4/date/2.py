import datetime 
yesterday=datetime.date.today()-datetime.timedelta(1)
today=datetime.date.today()
tomorrow=datetime.date.today()+datetime.timedelta(1)
print("Yesterday: ",yesterday,"Today: ", today , "Tomorrow: ", tomorrow)