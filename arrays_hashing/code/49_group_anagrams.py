class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # sorted : [strings]

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in groups:
                groups[sorted_s].append(s)
            else:
                groups[sorted_s] = [s]
        
        res = []
        for group in groups:
            res.append(groups[group])
        
        return res