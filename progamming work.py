NAGIRINYA PHIONAH BIOMEDICAL ENGINEERING 16/U/8330/ps
import datetime
years =float(input('Enter your age:'))
month=int(input('Enter month of birth:'))
day=int(input('Date of birth:'))
days_per_year=365.24ps
birthdate =datetime.datetime.now()  - datetime.timedelta(days=(years*days_per_year))
y=int(birthdate.strftime("%Y"))
x=datetime.date(y,month,day)
print(x.strftime("You were born on %A, %d-%B-%Y"))
