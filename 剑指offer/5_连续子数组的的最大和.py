# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值
# 要求时间复杂度为O(n)。
# 连续子数组：指在那个数组的连续的元素是连续截取出来的数组
# 动态规划
List = list


class Solution:
    def maxSubArray(self, nums: list):
        max_list = []
        for i in range(len(nums)):
            if len(max_list) == 0:
                z = nums[i]
            else:
                z = nums[i] + max_list[-1]  if max_list[-1] > 0 else nums[i]

            max_list.append(z)
        print(max_list)
        return max(max_list)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
for i in nums:
    continue
P = Solution()
z = P.maxSubArray(nums)
print(z)
