class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        s = s.lower()
        for char in s:
            if char.isalnum():
                clean += char
        length = (len(clean))
        for i in range(length):
            if clean[i] != clean[length - 1 - i]:
                return False
        return True