class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for ch in s.lower():
            if (ord(ch) >= 97 and ord(ch) <= 122) or (ord(ch) >=48 and ord(ch)<=57):
                 st+=ch
            else:
                continue
        return st == st[::-1]
    
