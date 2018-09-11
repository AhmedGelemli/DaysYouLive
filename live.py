import datetime

print("This program is showing you how many day are you living?")

print("When is your birthday?")
year = int(input('Year:'))
month = int(input('Month:'))
day = int(input('Day:'))

now_year = datetime.datetime.now().strftime("%Y")
now_month = datetime.datetime.now().strftime("%m")
now_days = datetime.datetime.now().strftime("%d")

if (int(now_year) < year or year < 1):
    print("-----------")
    print("Please try again! Please dont write year greater than '" + now_year +"' or less than '1'!")
    print("-----------")
elif (month > 12):
    print("-----------")
    print("Please try again! Please write month less than '12'!")
    print("-----------")
elif (day > 31):
    print("-----------")
    print("Please try again! Please write day less than '31'")
    print("-----------")
else:
    birth = datetime.date(year, month, day)
    now = datetime.date(int(now_year), int(now_month), int(now_days))
    print("------------")
    print(now - birth)
    print("------------")