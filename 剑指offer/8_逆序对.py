
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组，求出这个数组中的逆序对的总数。
#

# 输入: [7,5,6,4]
# 输出: 5


class Solution:
    def reversePairs(self, nums):
        add_nums = 0
        for index,num in enumerate(nums,1):
            nums_list = nums[index:]
            if nums_list:
                for num_1 in nums_list:
                    if num>num_1:
                        add_nums+=1
        return add_nums

Z =Solution()
w =Z.reversePairs([7,5,6,4])
print(w)