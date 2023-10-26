from datetime import date, timedelta
yest= date.today()-timedelta(1)
today=date.today()
tom=date.today()+timedelta(1)
print(yest)
print(today)
print(tom)
