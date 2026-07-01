class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myList = [-1 for i in range(1001)]
        myDict = dict()
        
        for i,num in enumerate(nums):
            if num in myDict.keys():
                return [myDict[num], i]
            myDict[target-num] = i

        