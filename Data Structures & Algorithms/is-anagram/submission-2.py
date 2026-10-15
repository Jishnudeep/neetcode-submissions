class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return True if sorted(s) == sorted(t) else False
        counter_s = [0] * 26
        counter_t = [0] * 26

        for ch in s:
            index_to_update = ord(ch) - ord("a")
            counter_s[index_to_update] += 1
        
        for ch in t:
            index_to_update = ord(ch) - ord("a")
            counter_t[index_to_update] += 1

        result = counter_s == counter_t

        return result