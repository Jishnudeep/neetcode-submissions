from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for word in strs: 
            counter = [0] * 26
            for ch in word:
                index_to_update = ord(ch) - ord("a")
                counter[index_to_update] += 1

            result[tuple(counter)].append(word)

        
        return list(result.values())