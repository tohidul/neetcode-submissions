from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)
        result = list()

        for s in strs:
            count_list = self.count_chars(s)
            result_dict[tuple(count_list)].append(s)
           
        for item in result_dict.keys():
            ana = result_dict[item]

            result.append(ana)
        
        return result
        
    def count_chars(self, my_str: str) -> list:
        result = [0]*26
        for s in my_str.lower():
            result[ord(s)-ord('a')]+=1
        return result