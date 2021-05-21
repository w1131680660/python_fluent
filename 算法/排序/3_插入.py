order_list = [23,1,123,2,4234,3,2]


def insert_order(or_list):

    for index, element in enumerate(order_list):
        if index + 1 < len(or_list):
            for num in range(index, -1, -1):
                if or_list[num] > order_list[num+1]:
                    order_list[num], order_list[num + 1] = order_list[num + 1], order_list[num]
                else:
                    break
    return or_list
zz = insert_order(order_list)
print(zz)