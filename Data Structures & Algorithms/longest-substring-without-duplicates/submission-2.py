class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        char_last_seen = dict()

        l = 0
        r = 0

        length = len(s)


        while r<length:
            last_count = char_last_seen.get(s[r])
            if last_count is not None and last_count >= l:
                
                if r-l > result:
                    result = r-l
                if last_count==l:
                    l+=1
                else:
                    l=r
            char_last_seen[s[r]] = r
            r+=1
        if r-l>result:
            result = r-l
        return result

        