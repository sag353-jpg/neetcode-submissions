class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in range(len(nums)):
            if nums[i] in frequency:
                frequency[nums[i]] += 1
            else:
                frequency[nums[i]] = 1
        i = 0
        final = []
        while k > 0:
            frequent = 0
            for key in frequency:
                if frequent < frequency[key]:
                    frequent = frequency[key]
            k -= 1
            for key in frequency:
                if frequency[key] == frequent:
                    pop = key
                    break
            final.append(pop)
            frequency.pop(pop)
        return final



        
        