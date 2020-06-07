import QuantLib as ql

# construction
peroid1 = ql.Period(3, ql.Months) # 3개월 정의
peroid2 = ql.Period(ql.Semiannual) # 특정 주기별로 이자를 지급하는 이자율스왑이나 통화 스왑 같은 상품을 구현하는 데에 있어서 자주 사용.

# Functions (transaction with Date)

date1 = ql.Date(11, 4, 2020)
date2 = ql.Date(31, 12, 2020)

three_weeks = ql.Period(3, ql.Weeks)
three_months = ql.Period(3, ql.Months)
three_years = ql.Period(3, ql.Years)

print('After 3 Weeks : {}'.format(date1 + three_weeks))
print('After 3 Months : {}'.format(date1 + three_months))
print('After 3 Years : {}'.format(date1 + three_years))

print('Days between Date2 and Date1 = {}'.format(date2 - date1))



