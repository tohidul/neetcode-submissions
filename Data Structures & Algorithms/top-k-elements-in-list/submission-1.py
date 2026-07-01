from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        result_freq = defaultdict(list)
        m = k

        result = [[] for _ in range(10000 + 1)]
        result2 = []

        for i in nums:
            freq[i]+=1
        for i in freq.keys():
            result[freq[i]].append(i)
        
        for item in  range(10000, 0, -1):
            if len(result[item])>0 and k>0:
                result2.extend(result[item][:k])
                k=k-len(result[item])
        return result2
        

        


        