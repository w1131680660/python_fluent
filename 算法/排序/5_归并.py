play_list = [323, 342, 123, 321, 324, 22, 12, 34, 531, 23213, 234, 2345454, 32224234, 131321,1]


def Merge_order(order_list):
    if len(order_list) ==1:
        return order_list
    len_list = len(order_list)
    mid = int(len_list/2)

    left = Merge_order(order_list[:mid])
    right = Merge_order(order_list[mid:])

    return marge(left, right)


def marge(left, right):
    result = []
    while len(left) >0 and len(right)>0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
       
    result += left
    result += right
    return result

z =Merge_order(play_list)
print(z)