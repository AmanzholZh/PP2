from datetime import *

first_date = datetime(2021, 2, 27, 17, 2, 39)
second_date = datetime(2021, 2, 27, 17, 2, 51)
year = int(first_date.strftime('%y'))
month = int(first_date.strftime('%m'))
day = int(first_date.strftime('%d'))
hour = int(first_date.strftime('%H'))
minute = int(first_date.strftime('%M'))
secund = ((int(second_date.strftime('%S')) - int(first_date.strftime('%S'))))
c = datetime(year,month, day,hour,minute,secund)
print(first_date.strftime('%d/%m/%y %H:%M:%S'), second_date.strftime('%d/%m/%y %H:%M:%S'))
print(c.strftime('%d/%m/%y %H:%M:%S'))