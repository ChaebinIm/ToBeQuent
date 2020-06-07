import QuantLib as ql

# Construction
us = ql.UnitedStates()
eu = ql.TARGET()
kr = ql.SouthKorea()
jp = ql.Japan()
cn = ql.China()

date1 = ql.Date(1, 1, 2020)
date2 = ql.Date(31, 12, 2020)
# 불완전할 수 있기에, 휴일을 추가할 수 있다.
kr.addHoliday(ql.Date(6, 5, 2020))
# 휴일 리스트를 만들어낼 수 있다. (정기적인 휴일은 모두 포함되어 있다)
kr_holidayList = kr.holidayList(date1, date2)
print(kr_holidayList)

# 영업일수를 나타내어 준다.
print(kr.businessDaysBetween(date1, date2))

# 영업일인지 아닌지 출력해준다.
print('Is it business day? ', kr.isBusinessDay(date1))
# 휴일인지 아닌지 출력해준다.
print('Is it holiday? ', kr.isHoliday(date1))


# 영업일 관행 -> 이론적 만기일과 휴일이 겹칠 경우의 관행 종류
# ql.Unadjusted, Preceding, ModifiedPreceding, Following, ModifiedFollowing
# 아래 예시에서 2월 28일에서 6개월 뒤가 8월 31일이 됨.
print(kr.advance(ql.Date(29, 2, 2020), ql.Period(6, ql.Months), ql.ModifiedFollowing, True)) # True는 월말기준(End of Month) 여부를 만족시킬 것인지 임.

# 중요 기능 : JointCalendar()
new_calendar = ql.JointCalendar(us, eu, kr)
print(new_calendar.holidayList(date1, date2))







