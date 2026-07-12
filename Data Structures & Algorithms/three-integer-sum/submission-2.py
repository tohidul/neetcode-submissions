class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = 0
        k = 0
        length = len(nums)
        result = []
        sorted_nums = sorted(nums)
        

        for i in range(length-2):
            j = i+1
            k = length - 1
            while j<k:
                if sorted_nums[i] == -(sorted_nums[j]+sorted_nums[k]):
                    temp = [sorted_nums[i], sorted_nums[j], sorted_nums[k]]
                    if temp not in result:
                        result.append(temp)
                    j+=1
                elif sorted_nums[j]+sorted_nums[k]+sorted_nums[i]>0:
                    k-=1
                else:
                    j+=1

        return result
