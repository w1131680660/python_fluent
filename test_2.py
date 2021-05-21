q = '胤佑秀耐-2146SA-罗秋丽-0113-T8806秀耐-海外仓建仓信息确认表.xlsx'
if '海外仓' in q:
    print(123)

# z = 'q-'
# w_1 = z.split('-')
# z = [i for i in w_1 if i]
# z.append(123)
# print(z, type(z))

import time
date = time.strftime("%d", time.localtime())
z ='15'
if z >= date:
    print(date)


import datetime
from dateutil.relativedelta import relativedelta
#获取当前日期的上一个月和后一个月
print(datetime.date.today())

from datetime import datetime as dt
value = '2017/01/7'

zzz= (dt.strptime(value, '%Y/%m/%d')- relativedelta(months=+1)).strftime("%Y/%m/%d")
print(zzz)
to_month = datetime.date.today().strftime("%Y-%m")
before_month = (datetime.date.today() - relativedelta(months=+1)).strftime("%Y-%m")
before_month_1 = (datetime.date.today() - relativedelta(months=+2)).strftime("%Y-%m")
before_month_2 = (datetime.date.today() - relativedelta(months=+3)).strftime("%Y-%m")
print( to_month, before_month, before_month_1,before_month_2 ,type(before_month_2))

qq ={'213':22}
print(qq.values())
from statistics import mean
zz = mean(qq.values())
print(zz)