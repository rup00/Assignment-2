import datetime
from time import strftime 
current_datetime=datetime.datetime.now()
date=current_datetime.strftime("%d-%m-%Y  %I:%M%p")
print(date)