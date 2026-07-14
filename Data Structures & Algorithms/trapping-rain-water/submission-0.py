class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        length = len(height)
        prefix.append(0)
        prefix_max = height[0]
        suffix_max = height[length-1]
        suffix.append(0)
        i = 1
        j=length-2
        result = 0

        for i in range(1,length):
            prefix.append(prefix_max)
            if height[i]>prefix_max:
                prefix_max = height[i]
            
        for j in range(length-2, -1, -1):
            suffix.append(suffix_max)
            if height[j]>suffix_max:
                suffix_max = height[j]
        j = -1
        for i in range(length):
            result+=max(0, min(prefix[i], suffix[j])-height[i])
            j-=1
        return result


        