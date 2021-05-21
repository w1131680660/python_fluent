

list_1= [1,23,23,2,323,23,121,123,]
index=23
def index_normal(list_1, target):
    result =[]
    for index,i in enumerate(list_1):
        if i == target:
            result.append(index)
    return result

result = index_normal(list_1, index)
print(result)

# 迭代器

def inter_normal(list_1, target):
    result = []
    for index ,i in enumerate(list_1):
        if i == target:
            yield index

result = inter_normal(list_1,index)
# 这里会返回iyig迭代器对象，需要list转换后才能被打印
print(list(result))