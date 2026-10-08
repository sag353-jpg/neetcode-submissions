class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i_seen = []
        for i in range(len(s)):
            i_seen.append(s[i])
        i_seen.sort()

        j_seen = []
        for j in range(len(t)):
            j_seen.append(t[j])
        j_seen.sort()

        if i_seen == j_seen:
            return True
        else:
            return False


        