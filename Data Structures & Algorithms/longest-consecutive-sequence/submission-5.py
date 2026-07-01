class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        length_of_largest_list = 0
        list_of_sequences = []
        length = 1
        for item in nums:
            if item-1 in num_set:
                tmp = item - 1
                while tmp in num_set:
                    length+=1
                    tmp = tmp-1
                length_of_largest_list = max(length_of_largest_list, length)
                length = 1
            else:
                length = 1
                length_of_largest_list = max(length_of_largest_list, length)
        return length_of_largest_list
                    


        