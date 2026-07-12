class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic_string = {}
        freq = [0] * 26
        result = []
        for str in strs:
            for char in str:
                freq[ord(char) - ord("a")] += 1
            fixed_freq = tuple(freq)
            if fixed_freq in dic_string:
                dic_string[fixed_freq].append(str)
            else:
                dic_string[fixed_freq] = [str]
            freq = [0] * 26
        return list(dic_string.values())
        
        