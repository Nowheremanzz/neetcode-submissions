class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic_string = {}
        freq = [0] * 26
        result = []
        i = 0
        for str in strs:
            for char in str:
                freq[ord(char) - ord("a")] += 1
            fixed_freq = tuple(freq)
            if fixed_freq in dic_string:
                result[dic_string[fixed_freq]].append(str)
            else:
                result.append([str])
                dic_string[fixed_freq] = i
                i += 1
            freq = [0] * 26
        return result
        
        