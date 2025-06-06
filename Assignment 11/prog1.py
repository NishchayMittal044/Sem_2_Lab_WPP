"""Write a Pandas program to create
a) Date time object for Jan 15 2012.
b) Specific date and time of 9:20 pm.
c) Local date and time.
d) A date without time.
e) Current date.
f) Time from a date time.
g) Current local time."""

import pandas as pd
from datetime import datetime,date,time

st_a=datetime(12,1,15)
print(st_a)

st_b=datetime(2012,1,15,21,20)
print(st_b)

st_c=datetime.now()
print(st_c)

st_d=date(2012,1,15)
print(st_d)

st_e=date.today()
print(st_e)

st_f=st_b.time()
print(st_f)

st_g=st_c.time()
print(st_g)

