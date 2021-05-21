
# 将format()函数和字符串方法是使得一个对象能够支持自定义方法的格式化
# 自定义格式化输出
_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code =='':
            code ='ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d =Date(2020,12,3)
z =format(d,'mdy')
print(z)

# 这些可以参考date类
from datetime import date
d = date(2021,12,21)
print(format(d))