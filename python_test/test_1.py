q = [{'name':'123'},{'name':'2323',},{'name':'2222'}]

# print(sorted(q,key=lambda q:q['name']))
# from itertools import groupby
# from operator import itemgetter
# print(sorted(q,key=itemgetter('name')))

z =a = """
 123
 abc
 456
 def
"""
import re
pattern= '\Adef'
print(re.findall(pattern,z))
