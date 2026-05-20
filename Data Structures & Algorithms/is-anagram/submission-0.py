class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_l = [x for x in s]
        t_l = [x for x in t]
        s_l.sort()
        t_l.sort()

        if len(s_l) != len(t_l):
            return False 

        for i in range(len(s_l)):
            if s_l[i] != t_l[i]:
                return False
        
        return True
        

        