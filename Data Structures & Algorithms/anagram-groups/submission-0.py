class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = []
        sorted = {}
        i = 0
        result = []
        for string in strs:
            letters = list(string)
            letters.sort()
            sorted_word = "".join(letters)
            sort.append(sorted_word)
        for sorted_word in sort:
            if sorted_word in sorted:
                sorted[sorted_word].append(strs[i])
                i = i + 1
            else:
                sorted[sorted_word] = [strs[i]]
                i = i + 1
        for key in sorted: 
            result.append(sorted[key])
        return result



        