class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix=1
        suffix=1
        for i in nums:
            result.append(prefix)
            prefix = prefix*i
        i = len(nums)-1
        while(i>=0):
            
            result[i]=result[i]*suffix
            suffix = nums[i]*suffix
            i-=1
        return result