class Solution:
    def isPalindrome(self, x: str) -> bool:
        l = 0
        r = len(x) - 1

        while l <= r:
            if x[l].isalnum() and x[r].isalnum():
                if x[l].lower() == x[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            else:
                if not x[l].isalnum():
                    l += 1
                if not x[r].isalnum():
                    r -= 1
        
        return True