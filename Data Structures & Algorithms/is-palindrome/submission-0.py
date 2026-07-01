class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_char_list = []
        filtered_char_list_reversed = []

        for c in s:
            if c.isalnum():
                filtered_char_list.append(c.lower())
        i = len(s)-1
        while(i>=0):
            c = s[i]
            if c.isalnum():
                filtered_char_list_reversed.append(c.lower())
            i-=1
        return filtered_char_list==filtered_char_list_reversed



        