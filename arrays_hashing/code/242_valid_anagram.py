class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
          

        s_table = {}
        t_table = {}
        

        for i in range(len(s)):
            s_table[s[i]] = s_table.get(s[i], 0) + 1
            t_table[t[i]] = t_table.get(t[i], 0) + 1
            
        
        return s_table == t_table
