import QuantLib as ql

# Basic Functions
date = ql.Date(11, 4, 2020)

dayOfMonth = date.dayOfMonth()
dayOfYear = date.dayOfYear()
month = date.month()
year = date.year()
serialNumber = date.serialNumber()
weekday = date.weekday()

print("Day of Month = {}".format(dayOfMonth))
print("Day of Year = {}".format(dayOfYear))
print("Month = {}".format(month))
print("Year = {}".format(year))
print("Serial Number = {}".format(serialNumber))
print("Weekday = {}".format(weekday))

print()

#Advanced Functions
date = ql.Date(12, 4, 2020)
todaysDate = date.todaysDate()
isLeap = date.isLeap(date.year())
isEndOfMonth = date.isEndOfMonth(date)
endOfMonth = date.endOfMonth(date)
nextWeekday = date.nextWeekday(date, 4) # 4번째 요일 = 수요일
nthWeekday = date.nthWeekday(3, 5, 7, 2020) # 2020년 7월 3째주 5번째요일

print("Today's Date = {}".format(todaysDate))
print("is Leap? = {}".format(isLeap))
print("is End of Month? = {}".format(isEndOfMonth))
print("End of Month = {}".format(endOfMonth))
print("Next Weekday = {}".format(nextWeekday))
print("Nth Weekday = {}".format(nthWeekday))
