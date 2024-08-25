import datetime

date_string= "Tue, 13 Aug 2024 09:02:00 +0900"

pdata = datetime.datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S +0900')
print(type(pdata))

pdata_string = pdata.strftime('%Y-%m-%d %H:%M:%S')
print(type(pdata_string))
print(pdata_string)