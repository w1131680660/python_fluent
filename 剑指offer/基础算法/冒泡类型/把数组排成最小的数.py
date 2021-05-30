class Solution:
    def minNumber(self, List):
        for index, num in enumerate(List):
            z_w =List[index+1:]
            for index_1,num_1 in enumerate(z_w,1):
                if num > num_1:
                    List[index],List[index+index_1] = List[index+index_1],List[index]
                    print(index+index_1,'---' ,List[index],List[index+index_1])
                    num =num_1
                    print(List)
        return List

z = [3,1,30,34,0,9]
q= Solution()
print(q.minNumber(z))